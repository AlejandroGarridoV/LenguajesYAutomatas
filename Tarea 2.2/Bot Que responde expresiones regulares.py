import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresiones regulares y respuestas asociadas
expresiones = {
    r"hello|hi|hey|hola": "¡Hola! ¿Cómo estás?",
    r"bye|adios|nos vemos": "¡Hasta luego!",
    r"bien|excelente|genial": "Me alegra escuchar eso.",
    r"mal|triste": "Espero que te sientas mejor pronto.",
    r"gracias": "¡De nada!",
    r"(\d{2})-(\d{2})-(\d{4})": "Esa parece ser una fecha en formato dd-mm-yyyy.",
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b": "Esa parece ser una dirección de correo electrónico válida.",
    r"\bhttps?://\S+\b": "Ese parece ser un enlace web.",
    r"\bme gusta\b (.*)": "¿Qué es lo que te gusta de {0}?",
    r"\bno me gusta\b (.*)": "¿Qué es lo que no te gusta de {0}?",
    r"\b(?:y tu|¿y tú|¿y tu?|Y tu?)\b": "Estoy bien, gracias por preguntar. ¿Qué estás haciendo tú?",
    r"\b\bsí\b": "¿Por qué sí?",
    r"\bno\b": "¿Por qué no?",
    r"\b(\w+)\b": "¿Te gusta '{0}'?"
}

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responder al mensaje si coincide con alguna expresión regular."""
    message_text = update.message.text
    for patron, respuesta in expresiones.items():
        coincidencias = re.findall(patron, message_text, re.IGNORECASE)
        for coincidencia in coincidencias:
            await update.message.reply_text(respuesta.format(coincidencia))
            return
    await update.message.reply_text("No entendí tu mensaje.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def main() -> None:
    """Iniciar el bot."""
    application = Application.builder().token("7173667891:AAFgV9fcWxer_mJUpsyUYRmfU3YJ_PpHMao").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
