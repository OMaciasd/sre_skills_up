from loguru import logger


def setup_logging():
    logger.add("./archivo.log", rotation="500 MB")

    logger.debug("Este es un mensaje de depuración")
    logger.info("Este es un mensaje informativo")
    logger.warning("Este es un mensaje de advertencia")
    logger.error("Este es un mensaje de error")
    logger.critical("Este es un mensaje crítico")

    logger.bind(usuario="Usuario1").info(
        "Este es un mensaje informativo con una etiqueta de usuario"
    )
    logger.info("Esto se guardará en el archivo")
