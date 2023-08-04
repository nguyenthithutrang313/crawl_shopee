from CommentCrawl import Comment_Shopee
import pandas as pd

product_info_df = pd.read_csv('C:\Workspace\Shopee\Code\P_banphim.csv')

if __name__ == "__main__":
    comment_crawler = Comment_Shopee()
    
    i=0
    for index, row in product_info_df.iterrows():
        item_id = row['itemid']
        shop_id = row['shopid']
        cmt_count = row['cmt_count']
        print(i)
        comment_crawler.crawl_comment(item_id, shop_id, cmt_count)
        i=i+1
    comment_crawler.save_csv('C_banphim.csv')