import json

def lambda_handler(event, context):
    result = {
        'current_datetime': '2022-12-07T20:42:40.857095',
        'extracted_text': 'St Lucie County Tribune April 6, 1906 CLEVELAND TO BUILD A HOME AT STUART Lately it has been learned that ex- President Grover Cleveland, who for many winters her been coming south to Stuart, in the northern part of Dade county, has purchased a plot of land in the town and will erect & substantial winter home thereon. The seller WAS Ernest Stypman and the deed will be re- curded in Miami within the next few days. says the Tropical Sun. All the world knows that Grover Cleveland la an enthuniastic fisherman and all the world knows also that Florida St Lucie County Tribune April 6, 1906 CLEVELAND TO BUILD A HOME AT STUART Lately it has been learned that ex- President Grover Cleveland, who for many winters her been coming south to Stuart, in the northern part of Dade county, has purchased a plot of land in the town and will erect & substantial winter home thereon. The seller WAS Ernest Stypman and the deed will be re- curded in Miami within the next few days. says the Tropical Sun. All the world knows that Grover Cleveland la an enthuniastic fisherman and all the world knows also that Florida',
        'original_summary': 'Ex-President Grover Cleveland has purchased a plot of land in Stuart, in the northern part of Dade county, and will erect a substantial winter home thereon . The seller WAS Ernest Stypman and the deed will be re-curded in Miami within the next few days . All the world knows that Grover . Cleveland la an enthuniastic fisherman and all the world . knows also that Florida .',
        'summary': '前总统格罗弗·克利夫兰在戴德县北部的斯图尔特购买了一块土地，并将在那里建造一座坚固的冬季住宅。卖方是欧内斯特·斯蒂普曼（Ernest Stypman），该契约将在接下来的几天内在迈阿密重新生效。全世界都知道格罗弗。克利夫兰是一位热情洋溢的渔民，也是全世界。也知道佛罗里达州。',
        'summary_language': 'zh',
        'input_user_id': 'adi',
        'input_language': 'zh',
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result),
        "isBase64Encoded": False
    } 