�
2�?Zc           @   sp  d  d l  m Z d  d l m Z d  d l Z d  d l  m Z d  d l m Z d  d l	 m
 Z
 d  d l m Z e d d	 � Z e e j d
  e j d
  d d d d �\ Z Z Z Z e d e
 d d d d � f d e �  f g � Z i e j d d d � d 6e j d  d d � d 6Z e e e d d d e d d d d  �Z e j e e � Z e j e j f e j e e � GHd S(    i����(   t   train_test_split(   t   fetch_20newsgroupsN(   t   GridSearchCV(   t   SVC(   t   TfidfVectorizer(   t   Pipelinet   subsett   alli�  t	   test_sizeg      �?t   random_statei!   t   vectt
   stop_wordst   englisht   analyzert   wordt   svci����i   i   t
   svc__gammai   t   svc__Ct   verbosei   t   refitt   cvt   n_jobs(   t   sklearn.model_selectionR    t   sklearn.datasetsR   t   numpyt   npR   t   sklearn.svmR   t   sklearn.feature_extraction.textR   t   sklearn.pipelineR   t   newst   datat   targett   X_traint   X_testt   y_traint   y_testt   clft   logspacet
   parameterst   Truet   gst   fitt   time_t   best_params_t   best_score_t   score(    (    (    s   D:\py\test3.pyt   <module>   s   502'