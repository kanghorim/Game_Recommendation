def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.df_reviews = pd.read_csv(
        './crawling_data/datasets/Game_reviews_ALL_Post.csv')
    self.Tfidf_matrix = mmread('./models/Tfidf_Game_review01.mtx').tocsr()
    with open('./models/tfidf01.pickle', 'rb') as f:
        self.Tfidf = pickle.load(f)
    self.titles = list(self.df_reviews['title'])
    self.titles.sort()
    for title in self.titles:
        self.cmb_titles.addItem(title)
    self.cmb_titles.currentIndexChanged.connect(
        self.cmb_titles_slot)
    self.pushButton.clicked.connect(self.btn_recommend_slot)