import  time, sys
from datetime import datetime, timedelta
from tools.util import send_pushplus
from loguru import logger
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/763a95312a1a4125b7cc431a041480dc"))

# If the transaction has not yet been mined, this method will raise a TransactionNotFound error.
receipt = w3.eth.get_transaction_receipt("0xa5724731cc891270334a6c9a64b388a0cbb5d8be8ad8f5550f86c16b197a5fd4")
if receipt["status"] != 1:
    # The transaction failed. DO NOT PROCEED
    pass

transaction = w3.eth.get_transaction("0xa5724731cc891270334a6c9a64b388a0cbb5d8be8ad8f5550f86c16b197a5fd4")


erc20_abi = '[{"inputs":[{"internalType":"uint256","name":"maxBatchSize_","type":"uint256"},{"internalType":"uint256","name":"collectionSize_","type":"uint256"},{"internalType":"uint256","name":"amountForDevs_","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"ApprovalToCurrentOwner","type":"error"},{"inputs":[],"name":"ApproveToCaller","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"a","type":"address"}],"name":"addAltar","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"amountForDevs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burnFromAltar","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"collectionSize","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"quantity","type":"uint256"}],"name":"devMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPrivateSaleOn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPublicSaleOn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPerAddressDuringMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"merkleRoot","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"quantity","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"numberMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"a","type":"address"}],"name":"removeAltar","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"saleConfig","outputs":[{"internalType":"uint32","name":"publicSaleStartTime","type":"uint32"},{"internalType":"uint64","name":"publicPriceWei","type":"uint64"},{"internalType":"uint32","name":"privateSaleStartTime","type":"uint32"},{"internalType":"uint64","name":"privatePriceWei","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_merkleRoot","type":"bytes32"}],"name":"setMerkleRoot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newMaxPerAddressDuringMint","type":"uint256"},{"internalType":"uint256","name":"newCollectionSize","type":"uint256"},{"internalType":"uint256","name":"newAmountForDevs","type":"uint256"}],"name":"setupCollectionInit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint64","name":"publicPriceWei","type":"uint64"},{"internalType":"uint32","name":"publicSaleStartTime","type":"uint32"},{"internalType":"uint64","name":"privatePriceWei","type":"uint64"},{"internalType":"uint32","name":"privateSaleStartTime","type":"uint32"}],"name":"setupSaleInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"bytes32[]","name":"_merkleProof","type":"bytes32[]"}],"name":"whitelistMint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"whitelistMintSig","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdrawMoney","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

# Get contract
token_contract_abi = json.loads(erc20_abi)
# Address is Goerli test net USD Coin contract address
token_contract = w3.eth.contract( abi=token_contract_abi)

transfer_function = token_contract.decode_function_input(transaction["input"])[0]
to_address = token_contract.decode_function_input(transaction["input"])[1]["_to"]
# Transfer value is in smallest denomination of token
transfer_value = token_contract.decode_function_input(transaction["input"])[1]["_value"]
from_address = transaction["from"]

# Backend needs to check to_address is platform address
if to_address != "<platform_address>":
    # Wrong address. DO NOT PROCEED
    pass

# Backend needs to verify transfer_function.
if getattr(transfer_function, "fn_name") != getattr(token_contract.functions.transfer, "fn_name"):
    # Wrong function. DO NOT PROCEED
    pass

# Backend needs to check database has from_address username.
# Backend write add transfer_value to user entry in database.

# logger.add('runtime.log')
#
#
#
# time1 = datetime.now() - timedelta(days=2)
# print(time1)
# logger.debug('this is a debug message')
# # print (datetime.datetime.now() > (datetime.datetime.now()-datetime.timedelta(weeks=4)))
# NOW = datetime.utcnow()
# print(NOW - timedelta(days=3))
# -------------------------------------------------------
# i = 0
#
# while True:
#     i = i+1
#     print('第{}次'.format(i))
#     print('2s')
#     time.sleep(2)
#
#     if i==2:
#         try:
#             1 / 0
#         except Exception as e:
#
#             try:
#                 title='测试'
#                 message = ""
#                 send_pushplus('异常通知', str(e), 'announcements')
#                 sys.exit(3)
#
#             except Exception as e1:
#
#                 print(e1)
#
#             sys.exit(3)
# -------------------------------------------------------
# current_year = datetime.datetime.today().strftime("%Y")
#
# def conv_time(t):
#     min = int(re.findall('T', t)[0])
#     if u'秒' in t:
#         s = (datetime.now() - datetime.timedelta(seconds=min))
#     elif u'分钟' in t:
#         s = (datetime.now() - datetime.timedelta(minutes=min))
#
#     elif u'小时' in t:
#         s = (datetime.now() - datetime.timedelta(hours=min))
#
#     elif u'天' in t:
#         s = (datetime.now() - datetime.timedelta(days=min))
#     else:
#         # t += ", " + current_year
#         s = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
#     return str(int(time.mktime(s.timetuple()))) + "000"
#
# a='2022-04-10T00:00:37.100Z'
# t= datetime.datetime.strptime(a, "%Y-%m-%dT%H:%M:%S.%fZ")
#
# diff = datetime.datetime.utcnow().timestamp() - t.timestamp()
#
# print(
#     int(diff//3600)
# )

# from util import get_random_useragent
# import svglib
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF, renderPM
# import tweepy
# import os, requests
# from config import global_config
#
#
# print ((datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y/%m/%d").replace('/','%2F'))
#
#
# def get_extension(url):
#     array = url.split('.')
#     return array[len(array)-1]
#
#
# def convert_filename(url):
#     if url[:-4]=='.svg':
#         drawing = svg2rlg("temp.svg")
#         png_path = 'temp.png'
#         renderPM.drawToFile(drawing, png_path, fmt="PNG")
#
# def tweet_image(url, message):
#
#
#
#     filename = 'temp.svg'
#     png_path = 'temp.png'
#     request = requests.get(url, stream=True, headers={'User-Agent': get_random_useragent()})
#     if request.status_code == 200:
#         with open(filename, 'wb') as image:
#             for chunk in request:
#                 image.write(chunk)
#
#
#
#
#         # renderPM.drawToFile(drawing, "drawing.jpg", fmt="JPG")
#
#         api.update_status_with_media(status=message, filename=png_path)
#         # os.remove(filename)
#     else:
#         print("Unable to download image")
#
# auth = tweepy.OAuthHandler(global_config.getRaw('twitter', 'consumer_key'),
#                            global_config.getRaw('twitter', 'consumer_secret'))
# auth.set_access_token(global_config.getRaw('twitter', 'key'),
#                       global_config.getRaw('twitter', 'secret'))
#
# api = tweepy.API(auth)
#
# message='我是兔子铃铛机器人,这是测试!请忽略'
#
# url='https://storage.googleapis.com/sentinel-nft/raw-assets/c39c5156ede40605d6567dc5cd81f644b4ffe1de5588264d3f746be93a23388d.svg'
#
# print(get_extension(url))
#
# re = tweet_image(url, message)
# print("转推结果：" + str(re.id_str))







# from pycoingecko import CoinGeckoAPI
#
# cg = CoinGeckoAPI()
#
# datas = cg.get_coins_markets('usd', order='gecko_desc',per_page=10, page=1)
#
# print(datas)


# import datetime, time
# timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")
# print (timestr)
#
#
# datetime.datetime.strptime(text, '%Y-%m-%d')
#
# timestr = time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime())
# print (timestr)
# from googletrans.client import Translator

# import translators as ts
import re
# import random
#
# tweets = [
#     'Wonderful promising project. This project is implemented very professionally and has a clear development plan. Without any doubt, this is one of the best project. Love this project. @PraptiSaad @reinkerte31 @yucm888888',
#     'It would be an honor to be a part of your project! You are frontrunners in the game, you have in me a loyal supporter who always gives. Keep it up, much love! @petechang1113 @abc_noName1 @kevinLiuA1110 @tastydogclub @Adidasshow78 @mike1021031',
#     '@Tony34108142 @waynechen2032 @Macnotmc1 @sodassdf @Ro0dZz @chou22389047 @stone20213  if my luck could ever carry me now would be the time',
#     '@itivitimonster @Malachi007 @Ivanyichen @SawadyQ @jayfans15 @RoyLiu68727021 @havel_wu Excited to be a part of it. Hopefully your first following will be WL and OGd for appreciation 🙏']
# message = random.choice(tweets)
# print(message)

# test_text = "k__Bacteria;p__@Verrucomicrobia ;c__@Verrucomicrobiae ;o__Verrucomicrobiales;f__Akkermansiaceae;g__Akkermansia;"
#
# species = re.findall(r'@(.+?)\s', test_text)
# print(''.join(species))

# wyw_text = 'Наш проект занимается поиском и разбором #Whitelist #IDO #ICO #Airdrop и тд.'
# chs_text = '季姬感到寂寞，罗集了一些鸡来养，鸡是那种出自荆棘丛中的野鸡。野鸡饿了唧唧叫，季姬就拿竹箕中的谷物喂鸡。'
# html_text = '''
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>我是标题</title>
# </head>
# <body>
# <p>我是文章《你的父亲》</p>
# </body>
# </html>
# '''
#
# # input languages
# print(ts.google(wyw_text, from_language='auto', to_language='zh-CN'))  # default: from_language='auto', to_language='en'

## output language_map
# print(ts._google.language_map)

