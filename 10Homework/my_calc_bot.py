from telegram import ForceReply, Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

import config
import calc_model


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""

    user = update.effective_user

    await update.message.reply_html(

        rf"""
    Hi {user.mention_html()}!
    Это бот-калькулятор
    Введите математическое выражение
    вида `/calc выражение`""",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /help is issued."""

    await update.message.reply_text("Введите команду вида `/calc выражение`")


async def calc_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(calc_model.calculate(update.message.text[6:]))


def main() -> None:
    """Start the bot."""
    bot_token = config.TOKEN

    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calc", calc_response))

    application.run_polling()


if __name__ == "__main__":

    main()

