import discord

client = discord.Client()  # 接続に使用するオブジェクト


# 起動時
@client.event
async def on_ready():
    print('ログイン成功')


# メッセージを監視
@client.event
async def on_message(message):
    # 「/box」が頭についたメッセージならオウム返しする
    if message.content.startswith('/box'):
        # 文字から「/box」を抜く
        question = message.content[len('/box'):].strip()
        # 質問させたいチャンネルのid
        target_channel_id = getTargetChannelId()

        # id=0なら質問者にエラー報告DM
        # idが0以外なら匿名質問する
        if target_channel_id == 0:
            dm = await message.author.create_dm()  # 質問者へDM作成
            await dm.send(
                'Sorry, メッセージを送信できませんでした．'
                'もう1度試してみてください．\n'
                '【質問文】' + question)
        else:
            # 匿名質問させたいチャンネル
            target_channel = client.get_channel(target_channel_id)
            # チャンネルに質問メッセージ送信
            await target_channel.send(question)

# botとしてDiscordに接続(botのトークンを指定)
client.run('TOKEN_OF_YOUR_BOT')
