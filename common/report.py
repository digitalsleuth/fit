#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# MIT License
#
# Copyright (c) 2022 FIT-Project and others
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----
######
import os


class ReportText:
    def __init__(self):
        self.TEXT = {
            'img': '..\\asset\\images\\FIT.png',
            'title': "FIT",
            'report': "Report Freezing Internet Tool",
            'version': "Versione 1.0 beta",
            'index': "Indice",

            'description': "FIT - Freezing Internet Tool è un’applicazione per l'acquisizione forense di contenuti "
                           "come pagine web, e-mail e social media direttamente da internet. <br><br>"
                           "Un browser forense è un software utilizzato per analizzare e recuperare dati da dispositivi elettronici, "
                           "come computer, smartphone o tablet, durante indagini forensi. Questo software consente di accedere a "
                           "informazioni sull'utilizzo del dispositivo, come cronologia delle attività, file e documenti, "
                           "messaggi di testo, immagini e molto altro, in modo da fornire prove che possono essere utilizzate "
                           "in una causa legale.",

            't1': "Freezing Internet Tool",
            't2': "Informazioni generali",
            'case': "Informazioni sul caso",
            'casedata': "Dati sul caso",
            'typed': "Tipo di acquisizione",
            'date': "Data acquisizione",

            't3': "Verifica titolarità dei dati",
            't3descr': "Nel corso dell'acquisizione, l'utente navigava alcuni siti web. FIT "
                       "procedeva alla verifica di ciascuna connessione mediante routine appositamente implementate. "
                       "In particolare, ai fini di stabilire la titolarità dei domini coinvolti, venivano indicate le "
                       "seguenti informazioni:",

            't4': "Digital Forensics",
            't4descr': "La digital forensics è l'applicazione scientifica e tecnologica dei principi "
                       "forensi alla raccolta, conservazione, analisi e presentazione dei dati digitali "
                       "in un contesto legale. Questa disciplina è utilizzata per investigare crimini informatici, "
                       "come la frode, il furto di dati o la diffusione di malware, e per recuperare e analizzare informazioni "
                       "da dispositivi elettronici come computer, smartphone e tablet. La digital forensics comprende "
                       "l'utilizzo di strumenti specializzati per analizzare i dati digitali e garantire la validità delle "
                       "prove in un contesto legale. Il lavoro dei professionisti della digital forensics è cruciale per "
                       "aiutare le agenzie investigative e i tribunali a identificare e punire i responsabili di crimini "
                       "informatici e garantire la giustizia.",

            'titlecc': "La Catena di Custodia",

            'ccdescr': "La catena di custodia è un concetto importante in ambito forense che descrive il "
                       "controllo e la documentazione degli spostamenti e delle manipolazioni di una prova "
                       "durante un'indagine o un processo legale. La catena di custodia garantisce che la prova sia autentica, "
                       "non alterata e non contaminata, e che la sua integrità sia mantenuta dal momento della raccolta fino "
                       "all'utilizzo in tribunale. Mantenere una catena di custodia affidabile è fondamentale per garantire "
                       "che la prova sia valida e adatta a supportare le conclusioni nell'ambito giudiziario.",

            'titleh': "Hash",
            'hdescr': "L'hash delle prove digitali è un valore univoco che rappresenta i dati "
                      "digitali e che viene utilizzato per verificare l'integrità e l'autenticità "
                      "delle prove. Un hash viene calcolato utilizzando un algoritmo di crittografia a "
                      "sensi unici che trasforma i dati in una stringa di caratteri a lunghezza fissa. Se i dati "
                      "originali vengono modificati, anche l'hash cambia, rendendo facile rilevare eventuali alterazioni. "
                      "In un contesto legale, l'hash delle prove digitali viene spesso utilizzato per verificare che i dati "
                      "originali non siano stati alterati durante il processo di raccolta, conservazione e presentazione delle "
                      "prove. Mantenere un record dell'hash delle prove digitali contribuisce a garantire la loro integrità "
                      "e ad assicurare che siano adatti a supportare le conclusioni in una causa legale.",

            't5': "File prodotti dal sistema",
            't5descr': "Durante l'acquisizione, il sistema ha prodotto una serie di file "
                       "(come screenshot, video dell'intera navigazione, log del traffico di rete, ecc.), identificati "
                       "nella seguente tabella.",

            'name': "Nome del file",
            'descr': "Descrizione",
            'avid': "Acquisizione video",
            'hashd': "File contenente gli hash dei file",
            'logd': "Informazioni generate dai vari componenti del sistema",
            'pcapd': "Registrazione del traffico di rete",
            'zipd': "Archivio contenente l'acquisizione",
            'txtd': "File whois",
            'pngd': "Screenshot della pagina",

            't6': "Hash dei file prodotti dal sistema",
            't6descr': "Ogni file prodotto dall'infrastruttura viene validato mediante il calcolo degli hash. "
                       "Con questa procedura, ogni singolo file prodotto è immodificabile e può essere fornito "
                       "anche singolarmente mantenendo la validità della Catena di Custodia",

            't7': "File prodotti dall'utente",
            't7descr': "Tutti i file prodotti dall'utente durante l'acquisizione sono raccolti all'interno "
                       "della cartella compressa avente estensione .zip. Per ognuno di questi file viene riportata "
                       "la dimensione espressa in bytes."
        }
        self.CASE = ["Cliente / Caso", "Avvocato", "Tipo di procedimento",
                     "Tribunale", "Numero di procedimento", "Tipo di acquisizione", "Data acquisizione"]