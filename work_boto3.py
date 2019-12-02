import logging
import warnings
import urllib3
import boto3
from boto3.dynamodb.conditions import Key, Attr

def main():
        # Logging
        logging.basicConfig(
            filename='./logs/work_basic.log',
            format='[%(asctime)s] %(levelname)s: %(name)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
            )
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Warning抑制
        warnings.simplefilter(
        'ignore', urllib3.exceptions.InsecureRequestWarning)            

        TABLE_SAKELIST = 'SAKE_LIST'
        MEIGARA_INDEX = 'meigara-index'
        MEIGARA_YOMI_INDEX = 'meigara_yomi-index'

        # AWS Credentialはwindows環境変数に設定.
        # proxy下だとSSLエラーが出るのでverify=false
        db = boto3.resource('dynamodb', verify=False)
        table = db.Table(TABLE_SAKELIST)

        # Table Status
        print("Table status:", table.table_status)

        # 単一アイテム取得. partition key, sort keyが必須.
        res = table.get_item(
            Key={'prefecture':'山梨県', 'meigara':'七賢'}
        )
        print('getItem: ', res['Item'])

        # partition key検索 .eqの一意検索が必要
        res = table.query(
            KeyConditionExpression=Key('prefecture').eq('香川県'),
            Limit=2
        )
        for row in res['Items']:
            print(row)

        # GSI(Global secondery index)検索
        res = table.query(
            IndexName=MEIGARA_INDEX,
            KeyConditionExpression=Key('meigara').eq('田酒')
        )
        for row in res['Items']:
            print(row)

if __name__ == "__main__":
    
    main()
