import discord
import os

client = discord.Client()  # 接続に使用するオブジェクト
token = os.environ['TOKEN_OF_YOUR_BOT']


# 起動時
@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


# メッセージを監視
@client.event
async def on_message(message):
    # 「/box」が頭についたメッセージならオウム返しする
    if message.content.startswith('/box'):
        # 文字から「/box」を抜く
        question = message.content[len('/box'):].strip()
        # 質問させたいチャンネルのid
        target_channel_id = 861529320383578112

        else:
            # 匿名質問させたいチャンネル
            target_channel = client.get_channel(target_channel_id)
            # チャンネルに質問メッセージ送信
            await target_channel.send(question)

# botとしてDiscordに接続(botのトークンを指定)
client.run(token)
