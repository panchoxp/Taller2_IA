# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import mysql.connector
from vaderSentiment.vaderSentiment  import SentimentIntensityAnalyzer
from googletrans import Translator

translator = Translator()
analyzer = SentimentIntensityAnalyzer()

con= mysql.connector.connect(host="LocalHost",user="root",password="S4panchoxp8399",database="clase_int_art")
cursor=con.cursor()

class ActionSaludos(Action):

    def name(self) -> Text:
        return "action_hello"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sql_insert= "INSERT INTO conversacion (id_usuario_conversacion, fecha_conversacion, polaridad_conversacion VALUES(%s,%s,%s))"

        texto = tracker.latest_message['text']
        traducido = translator.translate(texto, src="es", dest = "en").text
        sentiment = analyzer.polarity_scores(traducido)
        polaridad = "neutro"
        if sentiment["compound"] > 0:
            polaridad= "positivo"
        elif sentiment["compound"] < 0:
            polaridad= "negativo"
        valores=(tracker.sender_id,str(datetime.now()),polaridad)
        cursor.execute(sql_insert,valores)
        con.commit()
        dispatcher.utter_message(text="¡Hola! Soy el bot de juegos. ¿En qué puedo ayudarte?")
        return []

class ActionRecomendacion(Action):

    def name(self) -> Text:
        return "action_recomendacion_juego"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sql_insert= "INSERT INTO conversacion (id_usuario_conversacion, fecha_conversacion, polaridad_conversacion VALUES(%s,%s,%s))"

        texto = tracker.latest_message['text']
        traducido = translator.translate(texto, src="es", dest = "en").text
        sentiment = analyzer.polarity_scores(traducido)
        polaridad = "neutro"
        if sentiment["compound"] > 0:
            polaridad= "positivo"
        elif sentiment["compound"] < 0:
            polaridad= "negativo"
        valores=(tracker.sender_id,str(datetime.now()),polaridad)
        cursor.execute(sql_insert,valores)
        con.commit()
        dispatcher.utter_message(text="Claro, aquí tengo varios juegos que te pueden interesar: \n1. Assassins Creed \n2. God of War \n3. Resident Evil 4")
        return []

class ActionJuegoUno(Action):

    def name(self) -> Text:
        return "action_opinion_juego_1"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sql_insert= "INSERT INTO conversacion (id_usuario_conversacion, fecha_conversacion, polaridad_conversacion VALUES(%s,%s,%s))"

        texto = tracker.latest_message['text']
        traducido = translator.translate(texto, src="es", dest = "en").text
        sentiment = analyzer.polarity_scores(traducido)
        polaridad = "neutro"
        if sentiment["compound"] > 0:
            polaridad= "positivo"
        elif sentiment["compound"] < 0:
            polaridad= "negativo"
        valores=(tracker.sender_id,str(datetime.now()),polaridad)
        cursor.execute(sql_insert,valores)
        con.commit()
        dispatcher.utter_message(text="¡Genial! Te recomiendo probar Assassins Creed. ¿Te gustaría saber más sobre este juego?")
        return []

class ActionJuegoDos(Action):

    def name(self) -> Text:
        return "action_opinion_juego_2"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sql_insert= "INSERT INTO conversacion (id_usuario_conversacion, fecha_conversacion, polaridad_conversacion VALUES(%s,%s,%s))"

        texto = tracker.latest_message['text']
        traducido = translator.translate(texto, src="es", dest = "en").text
        sentiment = analyzer.polarity_scores(traducido)
        polaridad = "neutro"
        if sentiment["compound"] > 0:
            polaridad= "positivo"
        elif sentiment["compound"] < 0:
            polaridad= "negativo"
        valores=(tracker.sender_id,str(datetime.now()),polaridad)
        cursor.execute(sql_insert,valores)
        con.commit()
        dispatcher.utter_message(text="¡Genial! Te recomiendo probar God of War. ¿Te gustaría saber más sobre este juego?")
        return []

class ActionJuegoTres(Action):

    def name(self) -> Text:
        return "action_opinion_juego_3"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sql_insert= "INSERT INTO conversacion (id_usuario_conversacion, fecha_conversacion, polaridad_conversacion VALUES(%s,%s,%s))"

        texto = tracker.latest_message['text']
        traducido = translator.translate(texto, src="es", dest = "en").text
        sentiment = analyzer.polarity_scores(traducido)
        polaridad = "neutro"
        if sentiment["compound"] > 0:
            polaridad= "positivo"
        elif sentiment["compound"] < 0:
            polaridad= "negativo"
        valores=(tracker.sender_id,str(datetime.now()),polaridad)
        cursor.execute(sql_insert,valores)
        con.commit()
        dispatcher.utter_message(text="¡Genial! Te recomiendo probar Resident Evil 4. ¿Te gustaría saber más sobre este juego?")
        return []

class ActionDespedida(Action):

    def name(self) -> Text:
        return "action_despedida"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sql_insert= "INSERT INTO conversacion (id_usuario_conversacion, fecha_conversacion, polaridad_conversacion VALUES(%s,%s,%s))"

        texto = tracker.latest_message['text']
        traducido = translator.translate(texto, src="es", dest = "en").text
        sentiment = analyzer.polarity_scores(traducido)
        polaridad = "neutro"
        if sentiment["compound"] > 0:
            polaridad= "positivo"
        elif sentiment["compound"] < 0:
            polaridad= "negativo"
        valores=(tracker.sender_id,str(datetime.now()),polaridad)
        cursor.execute(sql_insert,valores)
        con.commit()
        dispatcher.utter_message(text="¡Adios! ¡Diviertete jugando! Vuelve pronto si necesitas mas ayuda.")
        return []