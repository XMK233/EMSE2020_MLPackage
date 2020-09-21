在这个爬虫里面，分两个分爬虫。

第一个爬取类型。也就是按照pytorch hub的filter来分类。因为有的模型属于两个类别：
两个，都是GAN的东西，它们既属于generative又属于vision。这个爬取类型得到的就是各种类别
下分别又什么module。

第二个爬取类型就是选择all类别，然后爬取所有的具体module内容。