import numpy as np
import scipy.stats
from sklearn.decomposition import LatentDirichletAllocation

class TextLDA:

    document_title_index = 'url' # 'title'

    #input- documents:[ {'title':string, 'dist'{string:non_negative integer ...} ... ]
    #       n_topics, n_iter: positive integer
    def __init__(self, documents, lda_object=None, n_topics=5, max_iter=1500, learning_method='batch', verbose=0, n_jobs=1, mean_change_tol=0.0001,random_state=None):
        self.vocab_list =[]

        for document in documents:
            self.vocab_list += document['dist'].keys()

        self.vocab_list = list(set(self.vocab_list))

        self.corpus_data = []

        for document in documents:
            word_counter = [0]*len(self.vocab_list)

            for word, count in document['dist'].items():
                word_counter[self.vocab_list.index(word)] = count

            self.corpus_data.append(word_counter)

        self.corpus_data  = np.array(self.corpus_data)


        self.model = LatentDirichletAllocation(n_topics=n_topics, max_iter=max_iter, n_jobs=n_jobs,
                                                   random_state=random_state, learning_method=learning_method,
                                                   mean_change_tol=mean_change_tol, verbose=verbose)


        self.topics = []
        self.n_iter = 0


    def initiate(self):
        # self.model.fit(corpus_data)
        """
        len_corpus = len(self.corpus_data)
        start_index = 0

        while start_index < len_corpus:

            end_index = start_index + 20 if start_index + 20 < len(self.corpus_data) else len_corpus
            self.model.partial_fit(self.corpus_data[start_index:end_index])
            start_index = start_index +20
        """
        topic_components = self.model.components_
        self.topics = []
        for word_dist in topic_components:
            sum_val = word_dist.sum()
            if sum_val > 0:
                word_dist = word_dist/sum_val*100.0
            self.topics.append({word:word_freq
                                for word, word_freq in zip(self.vocab_list, word_dist) if word_freq > 0.0})

        self.n_iter = self.model.n_iter_

        del self.corpus_data

    def get_query_score(self, keyword_list, g_documents, ex_documents):

        query_data = [0]*len(self.vocab_list)

        for keyword in keyword_list:
            if not keyword in self.vocab_list:
                continue
            query_data[self.vocab_list.index(keyword)] += 1

        query_data = np.array([query_data])
        query_lda = self.model.transform(query_data)
        query_topic_dist = query_lda[0]

        #document_list = self.documents


        google_result = dict()

        lda_document_order = list()

        for document in self.transform(g_documents):
            document_topic_dist = document['topic_dist']
            cos_lda_score = np.dot(query_topic_dist, document_topic_dist)/(np.linalg.norm(query_topic_dist)*np.linalg.norm(document_topic_dist))
            lda_score = (np.pi/2 - np.arccos(cos_lda_score))/(np.pi/2)*100
            google_result[document[self.document_title_index]] = lda_score
            lda_document_order.append(lda_score)

        order_score = list(range(len(g_documents)))[::-1]

        # if the number of documents is less than 2, then there is no correlation score, so just set the variable as 0
        spearman_cor = 0
        if len(order_score)> 1:
            spearman_cor = scipy.stats.spearmanr(order_score, lda_document_order)[0]

        compare_result = dict()

        if ex_documents:
            for document in self.transform(ex_documents):
                document_topic_dist = document['topic_dist']
                lda_score = np.dot(query_topic_dist, document_topic_dist)/(np.linalg.norm(query_topic_dist)*np.linalg.norm(document_topic_dist))

                compare_result[document[self.document_title_index]] = lda_score

        return {'query_topic_dist':query_topic_dist/query_topic_dist.sum()*100.0,'google_lda_scores':google_result, 'compare_lda_scores':compare_result, 'spearman_cor':spearman_cor}

    def get_topics(self):
        return self.topics

    def get_word_sorted_topics(self, num_words=None):

        if type(num_words)  != int or num_words < 1:
            return [sorted(topic.items(), key=lambda tup:tup[1], reverse=True)for topic in self.topics]
        else:
            return [sorted(topic.items(), key=lambda tup:tup[1], reverse=True)[0:num_words] for topic in self.topics]


    def get_sorted_documents(self, documents, num_topics=None):

        document_topic_dists = self.transform(documents)

        if type(num_topics) != int or num_topics < 1:
            return [{self.document_title_index:document[self.document_title_index], 'topics':list(np.argsort(np.array(document['topic_dist'])))} for document in document_topic_dists]

        return [{self.document_title_index:document[self.document_title_index], 'topics':list(np.argsort(document['topic_dist']))[0:num_topics]} for document in document_topic_dists]


    def transform(self, ex_documents):

        corpus_data = []

        for document in ex_documents:
            word_counter = [0]*len(self.vocab_list)

            for word, count in document['dist'].items():
                if not word in self.vocab_list:
                    continue
                word_counter[self.vocab_list.index(word)] = count

            corpus_data.append(word_counter)

        documents_topics = self.model.transform(np.array(corpus_data))

        res =[]

        for document, topic_dist in zip(ex_documents, documents_topics):
            sum_val = topic_dist.sum()
            if sum_val > 0:
                topic_dist = topic_dist/sum_val*100.0
            res.append({self.document_title_index:document[self.document_title_index], 'topic_dist':topic_dist})

        return res

