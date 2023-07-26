from ProductCrawl import Shopee
from CommentCrawl import Comment_Shopee


if __name__ == "__main__":
    product_crawler = Shopee()
    product_crawler.crawl_shopee(9)

    product_detail = product_crawler.product_detail_list

    comment_crawler = Comment_Shopee()
    
    dict = product_crawler.item_shop_dict

    i=0
    for item_id, item_info in dict.items():
        shop_id = item_info['shopid']
        cmt_count = item_info['cmtcount']
        print (f'Phase {i}')
        comment_crawler.crawl_comment(item_id, shop_id,cmt_count)
        i+=1
    product_crawler.save_csv('P_thietbidientu.csv')
    comment_crawler.save_csv('C_thietbidientu.csv')