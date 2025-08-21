
# import os
# import streamlit as st
# import pandas as pd
# from datetime import datetime
# from supabase import create_client
# from dotenv import load_dotenv
# import logging
# import re

# # -------------------------
# # Translation dictionary
# # -------------------------
# TRANSLATIONS = {
#     'en': {
#         'title': '🤝 Community Matcher',
#         'today': 'Today',
#         'navigation': 'Navigation',
#         'home': 'Home',
#         'register_beneficiary': 'Register Beneficiary',
#         'register_supporter': 'Register Supporter/Donor',
#         'reports': 'Reports',
#         'admin': 'Admin',
#         'language': 'Language',
#         'welcome_message': 'Welcome to the Community Matcher platform. Connect Beneficiaries with Supporters offering help.',
#         'system_status': 'System Status',
#         'features_disabled': 'Some features are disabled due to database issues:',
#         'admin_login': 'Admin Login',
#         'admin_email': 'Admin Email',
#         'admin_password': 'Admin Password',
#         'login_as_admin': 'Login as Admin',
#         'admin_logged_in': 'Admin logged in!',
#         'invalid_credentials': 'Invalid admin credentials',
#         'full_name': 'Full Name',
#         'date_of_birth': 'Date of Birth',
#         'address': 'Address',
#         'phone_number': 'Phone Number',
#         'email': 'Email',
#         'bank_account': 'Bank Account',
#         'relationship_to_org': 'Relationship to Organization',
#         'direct_beneficiary': 'Direct Beneficiary',
#         'family_member': 'Family Member',
#         'description_of_need': 'Description of Need or Support',
#         'declaration': 'I declare that the information is accurate and I consent to data use.',
#         'register_beneficiary_btn': 'Register Beneficiary',
#         'org_name': 'Full Name / Organization Name',
#         'contact_person': 'Contact Person (if organization)',
#         'type_of_support': 'Type of Support',
#         'financial': 'Financial',
#         'in_kind': 'In-Kind',
#         'volunteer': 'Volunteer',
#         'other': 'Other',
#         'donation_value': 'Donation Amount / Value',
#         'frequency': 'Frequency',
#         'one_time': 'One-time',
#         'monthly': 'Monthly',
#         'quarterly': 'Quarterly',
#         'annually': 'Annually',
#         'preferred_contact': 'Preferred Method of Contact',
#         'phone': 'Phone',
#         'mail': 'Mail',
#         'register_supporter_btn': 'Register Supporter',
#         'reports_dashboard': '📊 Reports Dashboard',
#         'summary': '📌 Summary',
#         'beneficiaries': 'Beneficiaries',
#         'supporters': 'Supporters',
#         'matches': 'Matches',
#         'download_csv': '⬇️ Download {table} CSV',
#         'no_records': 'No {table} records found.',
#         'success_registered': '{type} registered successfully!',
#         'failed_register': 'Failed to register {type}.',
#         'complete_required_fields': 'Please complete all required fields and agree to the declaration.',
#         'invalid_email': 'Invalid email format.',
#         'invalid_phone': 'Invalid phone number.',
#         'supabase_error': 'Supabase credentials missing. Put SUPABASE_URL and SUPABASE_KEY in a .env file.'
#     },
#     'de': {
#         'title': '🤝 Community Matcher',
#         'today': 'Heute',
#         'navigation': 'Navigation',
#         'home': 'Startseite',
#         'register_beneficiary': 'Begünstigten registrieren',
#         'register_supporter': 'Unterstützer/Spender registrieren',
#         'reports': 'Berichte',
#         'admin': 'Admin',
#         'language': 'Sprache',
#         'welcome_message': 'Willkommen bei der Community Matcher Plattform. Verbinden Sie Begünstigte mit Unterstützern, die Hilfe anbieten.',
#         'system_status': 'Systemstatus',
#         'features_disabled': 'Einige Funktionen sind aufgrund von Datenbankproblemen deaktiviert:',
#         'admin_login': 'Admin-Anmeldung',
#         'admin_email': 'Admin E-Mail',
#         'admin_password': 'Admin Passwort',
#         'login_as_admin': 'Als Admin anmelden',
#         'admin_logged_in': 'Admin angemeldet!',
#         'invalid_credentials': 'Ungültige Admin-Anmeldedaten',
#         'full_name': 'Vollständiger Name',
#         'date_of_birth': 'Geburtsdatum',
#         'address': 'Adresse',
#         'phone_number': 'Telefonnummer',
#         'email': 'E-Mail',
#         'bank_account': 'Bankkonto',
#         'relationship_to_org': 'Beziehung zur Organisation',
#         'direct_beneficiary': 'Direkter Begünstigter',
#         'family_member': 'Familienmitglied',
#         'description_of_need': 'Beschreibung des Bedarfs oder der Unterstützung',
#         'declaration': 'Ich erkläre, dass die Informationen korrekt sind und ich der Datennutzung zustimme.',
#         'register_beneficiary_btn': 'Begünstigten registrieren',
#         'org_name': 'Vollständiger Name / Organisationsname',
#         'contact_person': 'Kontaktperson (falls Organisation)',
#         'type_of_support': 'Art der Unterstützung',
#         'financial': 'Finanziell',
#         'in_kind': 'Sachleistung',
#         'volunteer': 'Freiwillig',
#         'other': 'Andere',
#         'donation_value': 'Spendenbetrag / Wert',
#         'frequency': 'Häufigkeit',
#         'one_time': 'Einmalig',
#         'monthly': 'Monatlich',
#         'quarterly': 'Vierteljährlich',
#         'annually': 'Jährlich',
#         'preferred_contact': 'Bevorzugte Kontaktmethode',
#         'phone': 'Telefon',
#         'mail': 'Post',
#         'register_supporter_btn': 'Unterstützer registrieren',
#         'reports_dashboard': '📊 Berichte Dashboard',
#         'summary': '📌 Zusammenfassung',
#         'beneficiaries': 'Begünstigte',
#         'supporters': 'Unterstützer',
#         'matches': 'Übereinstimmungen',
#         'download_csv': '⬇️ {table} CSV herunterladen',
#         'no_records': 'Keine {table}-Datensätze gefunden.',
#         'success_registered': '{type} erfolgreich registriert!',
#         'failed_register': 'Registrierung von {type} fehlgeschlagen.',
#         'complete_required_fields': 'Bitte füllen Sie alle Pflichtfelder aus und stimmen Sie der Erklärung zu.',
#         'invalid_email': 'Ungültiges E-Mail-Format.',
#         'invalid_phone': 'Ungültige Telefonnummer.',
#         'supabase_error': 'Supabase-Anmeldedaten fehlen. Setzen Sie SUPABASE_URL und SUPABASE_KEY in eine .env-Datei.'
#     },
#     'es': {
#         'title': '🤝 Community Matcher',
#         'today': 'Hoy',
#         'navigation': 'Navegación',
#         'home': 'Inicio',
#         'register_beneficiary': 'Registrar Beneficiario',
#         'register_supporter': 'Registrar Partidario/Donante',
#         'reports': 'Informes',
#         'admin': 'Admin',
#         'language': 'Idioma',
#         'welcome_message': 'Bienvenido a la plataforma Community Matcher. Conecta Beneficiarios con Partidarios que ofrecen ayuda.',
#         'system_status': 'Estado del Sistema',
#         'features_disabled': 'Algunas funciones están deshabilitadas debido a problemas de base de datos:',
#         'admin_login': 'Inicio de Sesión de Admin',
#         'admin_email': 'Email de Admin',
#         'admin_password': 'Contraseña de Admin',
#         'login_as_admin': 'Iniciar Sesión como Admin',
#         'admin_logged_in': '¡Admin conectado!',
#         'invalid_credentials': 'Credenciales de admin inválidas',
#         'full_name': 'Nombre Completo',
#         'date_of_birth': 'Fecha de Nacimiento',
#         'address': 'Dirección',
#         'phone_number': 'Número de Teléfono',
#         'email': 'Email',
#         'bank_account': 'Cuenta Bancaria',
#         'relationship_to_org': 'Relación con la Organización',
#         'direct_beneficiary': 'Beneficiario Directo',
#         'family_member': 'Miembro de la Familia',
#         'description_of_need': 'Descripción de Necesidad o Apoyo',
#         'declaration': 'Declaro que la información es precisa y consiento el uso de datos.',
#         'register_beneficiary_btn': 'Registrar Beneficiario',
#         'org_name': 'Nombre Completo / Nombre de Organización',
#         'contact_person': 'Persona de Contacto (si es organización)',
#         'type_of_support': 'Tipo de Apoyo',
#         'financial': 'Financiero',
#         'in_kind': 'En Especie',
#         'volunteer': 'Voluntario',
#         'other': 'Otro',
#         'donation_value': 'Cantidad de Donación / Valor',
#         'frequency': 'Frecuencia',
#         'one_time': 'Una vez',
#         'monthly': 'Mensual',
#         'quarterly': 'Trimestral',
#         'annually': 'Anual',
#         'preferred_contact': 'Método de Contacto Preferido',
#         'phone': 'Teléfono',
#         'mail': 'Correo',
#         'register_supporter_btn': 'Registrar Partidario',
#         'reports_dashboard': '📊 Panel de Informes',
#         'summary': '📌 Resumen',
#         'beneficiaries': 'Beneficiarios',
#         'supporters': 'Partidarios',
#         'matches': 'Coincidencias',
#         'download_csv': '⬇️ Descargar CSV de {table}',
#         'no_records': 'No se encontraron registros de {table}.',
#         'success_registered': '¡{type} registrado exitosamente!',
#         'failed_register': 'Error al registrar {type}.',
#         'complete_required_fields': 'Por favor complete todos los campos requeridos y acepte la declaración.',
#         'invalid_email': 'Formato de email inválido.',
#         'invalid_phone': 'Número de teléfono inválido.',
#         'supabase_error': 'Faltan credenciales de Supabase. Ponga SUPABASE_URL y SUPABASE_KEY en un archivo .env.'
#     },
#     'fr': {
#         'title': '🤝 Community Matcher',
#         'today': "Aujourd'hui",
#         'navigation': 'Navigation',
#         'home': 'Accueil',
#         'register_beneficiary': 'Inscrire un Bénéficiaire',
#         'register_supporter': 'Inscrire un Supporter/Donateur',
#         'reports': 'Rapports',
#         'admin': 'Admin',
#         'language': 'Langue',
#         'welcome_message': 'Bienvenue sur la plateforme Community Matcher. Connectez les Bénéficiaires avec les Supporters offrant de l\'aide.',
#         'system_status': 'État du Système',
#         'features_disabled': 'Certaines fonctionnalités sont désactivées en raison de problèmes de base de données:',
#         'admin_login': 'Connexion Admin',
#         'admin_email': 'Email Admin',
#         'admin_password': 'Mot de Passe Admin',
#         'login_as_admin': 'Se Connecter en tant qu\'Admin',
#         'admin_logged_in': 'Admin connecté!',
#         'invalid_credentials': 'Identifiants admin invalides',
#         'full_name': 'Nom Complet',
#         'date_of_birth': 'Date de Naissance',
#         'address': 'Adresse',
#         'phone_number': 'Numéro de Téléphone',
#         'email': 'Email',
#         'bank_account': 'Compte Bancaire',
#         'relationship_to_org': 'Relation avec l\'Organisation',
#         'direct_beneficiary': 'Bénéficiaire Direct',
#         'family_member': 'Membre de la Famille',
#         'description_of_need': 'Description du Besoin ou du Support',
#         'declaration': 'Je déclare que les informations sont exactes et je consens à l\'utilisation des données.',
#         'register_beneficiary_btn': 'Inscrire le Bénéficiaire',
#         'org_name': 'Nom Complet / Nom d\'Organisation',
#         'contact_person': 'Personne de Contact (si organisation)',
#         'type_of_support': 'Type de Support',
#         'financial': 'Financier',
#         'in_kind': 'En Nature',
#         'volunteer': 'Bénévole',
#         'other': 'Autre',
#         'donation_value': 'Montant de Don / Valeur',
#         'frequency': 'Fréquence',
#         'one_time': 'Une fois',
#         'monthly': 'Mensuel',
#         'quarterly': 'Trimestriel',
#         'annually': 'Annuel',
#         'preferred_contact': 'Méthode de Contact Préférée',
#         'phone': 'Téléphone',
#         'mail': 'Courrier',
#         'register_supporter_btn': 'Inscrire le Supporter',
#         'reports_dashboard': '📊 Tableau de Bord des Rapports',
#         'summary': '📌 Résumé',
#         'beneficiaries': 'Bénéficiaires',
#         'supporters': 'Supporters',
#         'matches': 'Correspondances',
#         'download_csv': '⬇️ Télécharger CSV {table}',
#         'no_records': 'Aucun enregistrement de {table} trouvé.',
#         'success_registered': '{type} inscrit avec succès!',
#         'failed_register': 'Échec de l\'inscription de {type}.',
#         'complete_required_fields': 'Veuillez remplir tous les champs obligatoires et accepter la déclaration.',
#         'invalid_email': 'Format d\'email invalide.',
#         'invalid_phone': 'Numéro de téléphone invalide.',
#         'supabase_error': 'Identifiants Supabase manquants. Mettez SUPABASE_URL et SUPABASE_KEY dans un fichier .env.'
#     },
#     'am': {  # Amharic
#         'title': '🤝 የማህበረሰብ ማገናኛ',
#         'today': 'ዛሬ',
#         'navigation': 'መሄጃ',
#         'home': 'ወደ ቤት',
#         'register_beneficiary': 'ተጠቃሚን መመዝገብ',
#         'register_supporter': 'ደጋፊ/ለጋሽ መመዝገብ',
#         'reports': 'ሪፖርቶች',
#         'admin': 'አስተዳዳሪ',
#         'language': 'ቋንቋ',
#         'welcome_message': 'ወደ የማህበረሰብ ማገናኛ መድረክ እንኳን በደህና መጡ። ተጠቃሚዎችን እርዳታ ከሚያቀርቡ ደጋፊዎች ጋር ያገናኙ።',
#         'system_status': 'የስርዓት ሁኔታ',
#         'features_disabled': 'በመረጃ ቋት ችግሮች ምክንያት አንዳንድ ባህሪያት ተሰናክለዋል:',
#         'admin_login': 'አስተዳዳሪ መግቢያ',
#         'admin_email': 'አስተዳዳሪ ኢሜይል',
#         'admin_password': 'አስተዳዳሪ የይለፍ ቃል',
#         'login_as_admin': 'እንደ አስተዳዳሪ ይግቡ',
#         'admin_logged_in': 'አስተዳዳሪ ገብቷል!',
#         'invalid_credentials': 'የተሳሳተ አስተዳዳሪ መረጃ',
#         'full_name': 'ሙሉ ስም',
#         'date_of_birth': 'የትውልድ ቀን',
#         'address': 'አድራሻ',
#         'phone_number': 'ስልክ ቁጥር',
#         'email': 'ኢሜይል',
#         'bank_account': 'የባንክ ሒሳብ',
#         'relationship_to_org': 'ከድርጅቱ ጋር ያለው ግንኙነት',
#         'direct_beneficiary': 'ቀጥተኛ ተጠቃሚ',
#         'family_member': 'የቤተሰብ አባል',
#         'description_of_need': 'የፍላጎት ወይም ድጋፍ መግለጫ',
#         'declaration': 'መረጃው ትክክል መሆኑን አረጋግጣለሁ እና ለመረጃ አጠቃቀም እስማማለሁ።',
#         'register_beneficiary_btn': 'ተጠቃሚን መመዝገብ',
#         'org_name': 'ሙሉ ስም / የድርጅት ስም',
#         'contact_person': 'የመገናኛ ሰው (ድርጅት ከሆነ)',
#         'type_of_support': 'የድጋፍ አይነት',
#         'financial': 'የገንዘብ',
#         'in_kind': 'እቃ',
#         'volunteer': 'በጎ ፈቃደኛ',
#         'other': 'ሌላ',
#         'donation_value': 'የልገሳ መጠን / ዋጋ',
#         'frequency': 'ድግግሞሽ',
#         'one_time': 'አንድ ጊዜ',
#         'monthly': 'ወርሃዊ',
#         'quarterly': 'ሩብ አመታዊ',
#         'annually': 'አመታዊ',
#         'preferred_contact': 'የተመረጠ የመገናኛ መንገድ',
#         'phone': 'ስልክ',
#         'mail': 'ፖስታ',
#         'register_supporter_btn': 'ደጋፊን መመዝገብ',
#         'reports_dashboard': '📊 የሪፖርቶች ዳሽቦርድ',
#         'summary': '📌 خلاصة',
#         'beneficiaries': 'ተጠቃሚዎች',
#         'supporters': 'ደጋፊዎች',
#         'matches': 'ግንኙነቶች',
#         'download_csv': '⬇️ {table} CSV አውርድ',
#         'no_records': 'የ{table} መዝገቦች አልተገኙም።',
#         'success_registered': '{type} በተሳካ ሁኔታ ተመዝግቧል!',
#         'failed_register': '{type} ማስመዝገብ አልተሳካም።',
#         'complete_required_fields': 'እባክዎ ሁሉንም አስፈላጊ መስኮች ይሙሉ እና ለመግለጫው ይስማሙ።',
#         'invalid_email': 'የተሳሳተ ኢሜይል ቅርፅ።',
#         'invalid_phone': 'የተሳሳተ ስልክ ቁጥር።',
#         'supabase_error': 'የSupabase ማረጋገጫዎች ተሰናክለዋል። SUPABASE_URL እና SUPABASE_KEY በ.env ፋይል ውስጥ ያስቀምጡ።'
#     },
#     'ti': {  # Tigrinya
#         'title': '🤝 ናይ ሕብረተሰብ ማሕበር',
#         'today': 'ሎሚ',
#         'navigation': 'መሳገሪ',
#         'home': 'ገዛ',
#         'register_beneficiary': 'ተጠቃሚ ምዝገባ',
#         'register_supporter': 'ደጋፊ/ዋሃቢ ምዝገባ',
#         'reports': 'ሪፖርታት',
#         'admin': 'ኣስተዳዳሪ',
#         'language': 'ቋንቋ',
#         'welcome_message': 'ናብ ናይ ሕብረተሰብ ማሕበር መድረኽ እንቋዕ ብደሓን መጻእኩም። ተጠቃማይ ምስ ሓገዛ ዚህቡ ደገፍቲ ኣሕሽሩ።',
#         'system_status': 'ሓበሬታ ስርዓት',
#         'features_disabled': 'ብሰበብ ናይ ዳታቤዝ ጸገማት ገለ ባህርያት ተዓጽዮም:',
#         'admin_login': 'ኣስተዳዳሪ መእተዊ',
#         'admin_email': 'ኣስተዳዳሪ ኢመይል',
#         'admin_password': 'ኣስተዳዳሪ ምስጢር ቃል',
#         'login_as_admin': 'ከም ኣስተዳዳሪ ኣቱ',
#         'admin_logged_in': 'ኣስተዳዳሪ ኣቲዩ!',
#         'invalid_credentials': 'ዘይቅኑዕ ናይ ኣስተዳዳሪ መረጋገጺ',
#         'full_name': 'ሙሉእ ስም',
#         'date_of_birth': 'ዕለት ልደት',
#         'address': 'ኣድራሻ',
#         'phone_number': 'ናይ ቴለፎን ቁጽሪ',
#         'email': 'ኢመይል',
#         'bank_account': 'ናይ ባንክ ሒሳብ',
#         'relationship_to_org': 'ምስ ውዳበ ዘሎ ዝምድና',
#         'direct_beneficiary': 'ቀጥተኛ ተጠቃሚ',
#         'family_member': 'ናይ ስድራቤት ኣባል',
#         'description_of_need': 'ናይ ድሌት ወይ ደገፍ መግለጺ',
#         'declaration': 'እቲ ሓበሬታ ቅኑዕ ምዃኑን ንኣጠቓቕማ መረጃ ዚሰማምዕ ምዃነይን የረጋግጽ።',
#         'register_beneficiary_btn': 'ተጠቃሚ ምዝገባ',
#         'org_name': 'ሙሉእ ስም / ናይ ውዳበ ስም',
#         'contact_person': 'ናይ ርክብ ሰብ (ውዳበ እንተኾይኑ)',
#         'type_of_support': 'ዓይነት ደገፍ',
#         'financial': 'ገንዘባዊ',
#         'in_kind': 'ንብረት',
#         'volunteer': 'ወላዳይነት',
#         'other': 'ካልእ',
#         'donation_value': 'መጠን ወይ ዋጋ ሃድነት',
#         'frequency': 'ድግግምነት',
#         'one_time': 'ሓደ ግዜ',
#         'monthly': 'ወርሓዊ',
#         'quarterly': 'ሩብዓዊ',
#         'annually': 'ዓመታዊ',
#         'preferred_contact': 'ዚመረጸ ናይ ርክብ ኣገባብ',
#         'phone': 'ቴለፎን',
#         'mail': 'ፖስታ',
#         'register_supporter_btn': 'ደጋፊ ምዝገባ',
#         'reports_dashboard': '📊 ናይ ሪፖርታት ዳሽቦርድ',
#         'summary': '📌 ሓፂር መግለጺ',
#         'beneficiaries': 'ተጠቃማይ',
#         'supporters': 'ደገፍቲ',
#         'matches': 'ርክባት',
#         'download_csv': '⬇️ {table} CSV ኣውርድ',
#         'no_records': 'ናይ {table} መዝገባት ኣይተረኽቡን።',
#         'success_registered': '{type} ብዓወት ተመዝጊቡ!',
#         'failed_register': '{type} ምዝገባ ኣይተሳካን።',
#         'complete_required_fields': 'በጃኹም ኩሎም ኣገደስቲ መስኮታት ምልኡን ንመግለጺ ሰማምዑን።',
#         'invalid_email': 'ዘይቅኑዕ ናይ ኢመይል ቅርጺ።',
#         'invalid_phone': 'ዘይቅኑዕ ናይ ቴለፎን ቁጽሪ።',
#         'supabase_error': 'ናይ Supabase መረጋገጺታት ጠፊኦም። SUPABASE_URL ከምኡውን SUPABASE_KEY ኣብ .env ፋይል ኣቐምጡ።'
#     }
# }

# # -------------------------
# # Translation helper function
# # -------------------------
# def get_text(key: str) -> str:
#     """Get translated text based on current language"""
#     lang = st.session_state.get('language', 'en')
#     return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)

# # -------------------------
# # Load config
# # -------------------------
# load_dotenv()
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# if not SUPABASE_URL or not SUPABASE_KEY:
#     st.error(get_text('supabase_error'))
#     st.stop()

# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# # -------------------------
# # Logging setup
# # -------------------------
# logging.basicConfig(level=logging.INFO, filename='app.log')
# logger = logging.getLogger(__name__)

# # -------------------------
# # Session state initialization
# # -------------------------
# for key, default in {
#     "Admin_authenticated": False,
#     "schema_warnings": [],
#     "matches_enabled": True,
#     "locks_enabled": True,
#     "language": "en"
# }.items():
#     if key not in st.session_state:
#         st.session_state[key] = default

# # -------------------------
# # Helper functions
# # -------------------------
# def insert_record(table: str, data: dict) -> bool:
#     try:
#         res = supabase.table(table).insert(data).execute()
#         if hasattr(res, "data") and res.data:
#             logger.info(f"Inserted record into {table}: {res.data}")
#             return True
#         return False
#     except Exception as e:
#         logger.error(f"Insert failed for {table}: {str(e)}")
#         return False

# def fetch_table(table: str) -> pd.DataFrame:
#     try:
#         res = supabase.table(table).select("*").execute()
#         if hasattr(res, "data") and res.data:
#             return pd.DataFrame(res.data)
#         return pd.DataFrame()
#     except Exception as e:
#         logger.error(f"Fetch failed for {table}: {str(e)}")
#         return pd.DataFrame()

# def is_valid_email(email):
#     return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# def is_valid_phone(phone):
#     return re.match(r"^\+?\d{7,15}$", phone)

# def mask_account(account):
#     return f"****{account[-4:]}" if account else ""

# # -------------------------
# # Schema validation
# # -------------------------
# def validate_schema():
#     critical_tables = [
#         ("beneficiaries", {"id", "full_name", "phone_number", "status", "bank_account"}),
#         ("supporters", {"id", "organization_name", "phone_number", "status"})
#     ]
#     optional_tables = [
#         ("matches", {"beneficiary_id", "supporter_id", "matched_at"}),
#         ("locks", {"lock_name", "is_locked", "locked_at"})
#     ]
#     warnings = []
#     for table, required_cols in critical_tables + optional_tables:
#         df = fetch_table(table)
#         if not df.empty and not required_cols.issubset(df.columns):
#             warnings.append(f"Table {table} missing required columns: {required_cols - set(df.columns)}")
#             logger.warning(f"Schema warning for table {table}: {warnings[-1]}")
#     st.session_state["schema_warnings"] = warnings
# validate_schema()

# # -------------------------
# # Streamlit UI
# # -------------------------
# st.set_page_config(page_title="Community Matcher", layout="wide")

# # Language selector at the top
# col1, col2 = st.columns([3, 1])
# with col1:
#     st.title(get_text('title'))
#     st.caption(f"📅 {get_text('today')}: {datetime.today().strftime('%B %d, %Y')}")

# with col2:
#     language_options = {
#         'en': '🇺🇸 English',
#         'de': '🇩🇪 Deutsch', 
#         'es': '🇪🇸 Español',
#         'fr': '🇫🇷 Français',
#         'am': '🇪🇹 አማርኛ',
#         'ti': '🇪🇷 ትግርኛ'
#     }
    
#     selected_lang = st.selectbox(
#         get_text('language'),
#         options=list(language_options.keys()),
#         format_func=lambda x: language_options[x],
#         index=list(language_options.keys()).index(st.session_state.get('language', 'en'))
#     )
    
#     if selected_lang != st.session_state.get('language'):
#         st.session_state['language'] = selected_lang
#         st.rerun()

# # -------------------------
# # Sidebar navigation
# # -------------------------
# menu = st.sidebar.radio(get_text('navigation'), [
#     get_text('home'), 
#     get_text('register_beneficiary'), 
#     get_text('register_supporter'), 
#     get_text('reports'), 
#     get_text('admin')
# ])

# # -------------------------
# # Admin login only on Admin page
# # -------------------------
# if menu == get_text('admin') and not st.session_state["Admin_authenticated"]:
#     st.subheader(get_text('admin_login'))
#     with st.form("admin_login_form"):
#         admin_email = st.text_input(get_text('admin_email'))
#         admin_password = st.text_input(get_text('admin_password'), type="password")
#         admin_login_button = st.form_submit_button(get_text('login_as_admin'))
#         if admin_login_button:
#             if admin_email == "admin@example.com" and admin_password == "admin123":
#                 st.session_state["Admin_authenticated"] = True
#                 st.success(get_text('admin_logged_in'))
#                 st.rerun()
#             else:
#                 st.error(get_text('invalid_credentials'))
#     st.stop()

# # -------------------------
# # Pages
# # -------------------------
# if menu == get_text('home'):
#     st.markdown(get_text('welcome_message'))
#     if st.session_state["schema_warnings"]:
#         with st.expander(get_text('system_status'), expanded=True):
#             st.warning(get_text('features_disabled'))
#             for warning in st.session_state["schema_warnings"]:
#                 st.write(f"- {warning}")

# elif menu == get_text('register_beneficiary'):
#     st.subheader(get_text('register_beneficiary'))
#     with st.form("beneficiary_form"):
#         full_name = st.text_input(get_text('full_name'))
#         dob = st.date_input(get_text('date_of_birth'))
#         address = st.text_area(get_text('address'))
#         phone = st.text_input(get_text('phone_number'))
#         email = st.text_input(get_text('email'))
#         bank_account = st.text_input(get_text('bank_account'))
#         relationship = st.selectbox(get_text('relationship_to_org'), [get_text('direct_beneficiary'), get_text('family_member')])
#         description = st.text_area(get_text('description_of_need'))
#         declaration = st.checkbox(get_text('declaration'))
#         submit = st.form_submit_button(get_text('register_beneficiary_btn'))
#         if submit:
#             if full_name and phone and declaration:
#                 if email and not is_valid_email(email):
#                     st.error(get_text('invalid_email'))
#                 elif not is_valid_phone(phone):
#                     st.error(get_text('invalid_phone'))
#                 else:
#                     data = {
#                         "full_name": full_name,
#                         "date_of_birth": dob.strftime("%Y-%m-%d"),
#                         "address": address,
#                         "phone_number": phone,
#                         "email": email,
#                         "bank_account": bank_account,
#                         "relationship_to_org": relationship,
#                         "description_of_need": description,
#                         "declaration_consent": True,
#                         "submitted_at": datetime.now().isoformat(),
#                         "status": "Pending"
#                     }
#                     if insert_record("beneficiaries", data):
#                         st.success(get_text('success_registered').format(type=get_text('beneficiaries')))
#                     else:
#                         st.error(get_text('failed_register').format(type=get_text('beneficiaries')))
#             else:
#                 st.error(get_text('complete_required_fields'))

# elif menu == get_text('register_supporter'):
#     st.subheader(get_text('register_supporter'))
#     with st.form("supporter_form"):
#         org_name = st.text_input(get_text('org_name'))
#         contact_person = st.text_input(get_text('contact_person'))
#         address = st.text_area(get_text('address'))
#         phone = st.text_input(get_text('phone_number'))
#         email = st.text_input(get_text('email'))
#         support_type = st.multiselect(get_text('type_of_support'), [
#             get_text('financial'), 
#             get_text('in_kind'), 
#             get_text('volunteer'), 
#             get_text('other')
#         ])
#         donation_value = st.text_input(get_text('donation_value'))
#         frequency = st.selectbox(get_text('frequency'), [
#             get_text('one_time'), 
#             get_text('monthly'), 
#             get_text('quarterly'), 
#             get_text('annually')
#         ])
#         preferred_contact = st.selectbox(get_text('preferred_contact'), [
#             get_text('email'), 
#             get_text('phone'), 
#             get_text('mail')
#         ])
#         declaration = st.checkbox(get_text('declaration'))
#         submit = st.form_submit_button(get_text('register_supporter_btn'))
#         if submit:
#             if org_name and phone and declaration:
#                 if email and not is_valid_email(email):
#                     st.error(get_text('invalid_email'))
#                 elif not is_valid_phone(phone):
#                     st.error(get_text('invalid_phone'))
#                 else:
#                     data = {
#                         "organization_name": org_name,
#                         "contact_person": contact_person,
#                         "address": address,
#                         "phone_number": phone,
#                         "email": email,
#                         "type_of_support": ", ".join(support_type),
#                         "donation_value": donation_value,
#                         "frequency": frequency,
#                         "preferred_contact": preferred_contact,
#                         "declaration_consent": True,
#                         "submitted_at": datetime.now().isoformat(),
#                         "status": "Pending"
#                     }
#                     if insert_record("supporters", data):
#                         st.success(get_text('success_registered').format(type=get_text('supporters')))
#                     else:
#                         st.error(get_text('failed_register').format(type=get_text('supporters')))
#             else:
#                 st.error(get_text('complete_required_fields'))

# elif menu == get_text('reports'):
#     st.subheader(get_text('reports_dashboard'))

#     # Fetch data
#     b_df = fetch_table("beneficiaries")
#     s_df = fetch_table("supporters")
#     m_df = fetch_table("matches")

#     # Mask bank accounts
#     if not b_df.empty and "bank_account" in b_df.columns:
#         b_df["bank_account"] = b_df["bank_account"].apply(mask_account)

#     # Summary stats
#     st.markdown(f"### {get_text('summary')}")
#     col1, col2, col3 = st.columns(3)
#     col1.metric(get_text('beneficiaries'), len(b_df))
#     col2.metric(get_text('supporters'), len(s_df))
#     col3.metric(get_text('matches'), len(m_df))

#     st.markdown("---")

#     # Beneficiaries Section
#     st.markdown(f"### 🧍 {get_text('beneficiaries')}")
#     if not b_df.empty:
#         st.dataframe(b_df, use_container_width=True)
#         st.download_button(
#             get_text('download_csv').format(table=get_text('beneficiaries')), 
#             b_df.to_csv(index=False), 
#             "beneficiaries.csv"
#         )
#     else:
#         st.info(get_text('no_records').format(table=get_text('beneficiaries').lower()))

#     st.markdown("---")

#     # Supporters Section
#     st.markdown(f"### 🤝 {get_text('supporters')}")
#     if not s_df.empty:
#         st.dataframe(s_df, use_container_width=True)
#         st.download_button(
#             get_text('download_csv').format(table=get_text('supporters')), 
#             s_df.to_csv(index=False), 
#             "supporters.csv"
#         )
#     else:
#         st.info(get_text('no_records').format(table=get_text('supporters').lower()))

#     st.markdown("---")

#     # Matches Section
#     st.markdown(f"### 🔗 {get_text('matches')}")
#     if st.session_state.get("matches_enabled", True):
#         if not m_df.empty:
#             st.dataframe(m_df, use_container_width=True)
#             st.download_button(
#                 get_text('download_csv').format(table=get_text('matches')), 
#                 m_df.to_csv(index=False), 
#                 "matches.csv"
#             )
#         else:
#             st.info(get_text('no_records').format(table=get_text('matches').lower()))
import os
import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv
import logging
import re

# -------------------------
# Translation dictionary
# -------------------------
TRANSLATIONS = {
    'en': {
        'title': '🤝 BetterTogether',
        'today': 'Today',
        'navigation': 'Navigation',
        'home': 'Home',
        'register_beneficiary': 'Register Beneficiary',
        'register_supporter': 'Register Supporter/Donor',
        'reports': 'Reports',
        "reports": "Reports",
        "reports_dashboard": "Reports Dashboard",
        "required_to_access": "is required to access this page.",

        'admin': 'Admin',
        'language': 'Language',
        'welcome_message': 'Welcome to the BetterTogether platform. Connect Beneficiaries with Supporters offering help.',
        'system_status': 'System Status',
        'features_disabled': 'Some features are disabled due to database issues:',
        'admin_login': 'Admin Login',
        'admin_email': 'Admin Email',
        'admin_password': 'Admin Password',
        'login_as_admin': 'Login as Admin',
        'admin_logged_in': 'Admin logged in!',
        'invalid_credentials': 'Invalid admin credentials',
        'full_name': 'Full Name',
        'date_of_birth': 'Date of Birth',
        'address': 'Address',
        'phone_number': 'Phone Number',
        'email': 'Email',
        'bank_account': 'Bank Account',
        'relationship_to_org': 'Relationship to Organization',
        'direct_beneficiary': 'Direct Beneficiary',
        'family_member': 'Family Member',
        'description_of_need': 'Description of Need or Support',
        'declaration': 'I declare that the information is accurate and I consent to data use.',
        'register_beneficiary_btn': 'Register Beneficiary',
        'org_name': 'Full Name / Organization Name',
        'contact_person': 'Contact Person (if organization)',
        'type_of_support': 'Type of Support',
        'financial': 'Financial',
        'in_kind': 'In-Kind',
        'volunteer': 'Volunteer',
        'other': 'Other',
        'donation_value': 'Donation Amount / Value',
        'frequency': 'Frequency',
        'one_time': 'One-time',
        'monthly': 'Monthly',
        'quarterly': 'Quarterly',
        'annually': 'Annually',
        'preferred_contact': 'Preferred Method of Contact',
        'phone': 'Phone',
        'mail': 'Mail',
        'register_supporter_btn': 'Register Supporter',
        'reports_dashboard': '📊 Reports Dashboard',
        'summary': '📌 Summary',
        'beneficiaries': 'Beneficiaries',
        'supporters': 'Supporters',
        'matches': 'Matches',
        'download_csv': '⬇️ Download {table} CSV',
        'no_records': 'No {table} records found.',
        'success_registered': '{type} registered successfully!',
        'failed_register': 'Failed to register {type}.',
        'complete_required_fields': 'Please complete all required fields and agree to the declaration.',
        'invalid_email': 'Invalid email format.',
        'invalid_phone': 'Invalid phone number.',
        'supabase_error': 'Supabase credentials missing. Put SUPABASE_URL and SUPABASE_KEY in a .env file.',
        'contact_admin': 'Contact Admin',
        'contact_us': 'Contact Us',
        'help_support': 'Help & Support',
        'subject': 'Subject',
        'message': 'Message',
        'urgent': 'Urgent',
        'general_inquiry': 'General Inquiry',
        'technical_issue': 'Technical Issue',
        'registration_help': 'Registration Help',
        'data_correction': 'Data Correction',
        'send_message': 'Send Message',
        'message_sent': 'Message sent successfully!',
        'message_failed': 'Failed to send message.',
        'admin_contact_info': 'Admin Contact Information',
        'phone_contact': 'Phone Contact',
        'email_contact': 'Email Contact',
        'office_hours': 'Office Hours',
        'emergency_contact': 'Emergency Contact',
        'faq': 'Frequently Asked Questions',
        'how_to_register': 'How to register?',
        'forgot_password': 'Forgot password?',
        'update_info': 'How to update my information?'
    },
    'de': {
        'title': '🤝 BetterTogether',
        'today': 'Heute',
        'navigation': 'Navigation',
        'home': 'Startseite',
        'register_beneficiary': 'Begünstigten registrieren',
        'register_supporter': 'Unterstützer/Spender registrieren',
        'reports': 'Berichte',
        'admin': 'Admin',
        'language': 'Sprache',
        'welcome_message': 'Willkommen bei der BetterTogether Plattform. Verbinden Sie Begünstigte mit Unterstützern, die Hilfe anbieten.',
        'system_status': 'Systemstatus',
        'features_disabled': 'Einige Funktionen sind aufgrund von Datenbankproblemen deaktiviert:',
        'admin_login': 'Admin-Anmeldung',
        'admin_email': 'Admin E-Mail',
        'admin_password': 'Admin Passwort',
        'login_as_admin': 'Als Admin anmelden',
        'admin_logged_in': 'Admin angemeldet!',
        'invalid_credentials': 'Ungültige Admin-Anmeldedaten',
        'full_name': 'Vollständiger Name',
        'date_of_birth': 'Geburtsdatum',
        'address': 'Adresse',
        'phone_number': 'Telefonnummer',
        'email': 'E-Mail',
        'bank_account': 'Bankkonto',
        'relationship_to_org': 'Beziehung zur Organisation',
        'direct_beneficiary': 'Direkter Begünstigter',
        'family_member': 'Familienmitglied',
        'description_of_need': 'Beschreibung des Bedarfs oder der Unterstützung',
        'declaration': 'Ich erkläre, dass die Informationen korrekt sind und ich der Datennutzung zustimme.',
        'register_beneficiary_btn': 'Begünstigten registrieren',
        'org_name': 'Vollständiger Name / Organisationsname',
        'contact_person': 'Kontaktperson (falls Organisation)',
        'type_of_support': 'Art der Unterstützung',
        'financial': 'Finanziell',
        'in_kind': 'Sachleistung',
        'volunteer': 'Freiwillig',
        'other': 'Andere',
        'donation_value': 'Spendenbetrag / Wert',
        'frequency': 'Häufigkeit',
        'one_time': 'Einmalig',
        'monthly': 'Monatlich',
        'quarterly': 'Vierteljährlich',
        'annually': 'Jährlich',
        'preferred_contact': 'Bevorzugte Kontaktmethode',
        'phone': 'Telefon',
        'mail': 'Post',
        'register_supporter_btn': 'Unterstützer registrieren',
        'reports_dashboard': '📊 Berichte Dashboard',
        'summary': '📌 Zusammenfassung',
        'beneficiaries': 'Begünstigte',
        'supporters': 'Unterstützer',
        'matches': 'Übereinstimmungen',
        'download_csv': '⬇️ {table} CSV herunterladen',
        'no_records': 'Keine {table}-Datensätze gefunden.',
        'success_registered': '{type} erfolgreich registriert!',
        'failed_register': 'Registrierung von {type} fehlgeschlagen.',
        'complete_required_fields': 'Bitte füllen Sie alle Pflichtfelder aus und stimmen Sie der Erklärung zu.',
        'invalid_email': 'Ungültiges E-Mail-Format.',
        'invalid_phone': 'Ungültige Telefonnummer.',
        'supabase_error': 'Supabase-Anmeldedaten fehlen. Setzen Sie SUPABASE_URL und SUPABASE_KEY in eine .env-Datei.',
        'contact_admin': 'Admin Kontaktieren',
        'contact_us': 'Kontaktieren Sie uns',
        'help_support': 'Hilfe und Support',
        'subject': 'Betreff',
        'message': 'Nachricht',
        'urgent': 'Dringend',
        'general_inquiry': 'Allgemeine Anfrage',
        'technical_issue': 'Technisches Problem',
        'registration_help': 'Registrierungshilfe',
        'data_correction': 'Datenkorrektur',
        'send_message': 'Nachricht Senden',
        'message_sent': 'Nachricht erfolgreich gesendet!',
        'message_failed': 'Nachricht konnte nicht gesendet werden.',
        'admin_contact_info': 'Admin-Kontaktinformationen',
        'phone_contact': 'Telefonkontakt',
        'email_contact': 'E-Mail-Kontakt',
        'office_hours': 'Bürozeiten',
        'emergency_contact': 'Notfallkontakt',
        'faq': 'Häufig Gestellte Fragen',
        'how_to_register': 'Wie registriere ich mich?',
        'forgot_password': 'Passwort vergessen?',
        'update_info': 'Wie aktualisiere ich meine Informationen?'
    },
    'es': {
        'title': '🤝 BetterTogether',
        'today': 'Hoy',
        'navigation': 'Navegación',
        'home': 'Inicio',
        'register_beneficiary': 'Registrar Beneficiario',
        'register_supporter': 'Registrar Partidario/Donante',
        'reports': 'Informes',
        'admin': 'Admin',
        'language': 'Idioma',
        'welcome_message': 'Bienvenido a la plataforma BetterTogether. Conecta Beneficiarios con Partidarios que ofrecen ayuda.',
        'system_status': 'Estado del Sistema',
        'features_disabled': 'Algunas funciones están deshabilitadas debido a problemas de base de datos:',
        'admin_login': 'Inicio de Sesión de Admin',
        'admin_email': 'Email de Admin',
        'admin_password': 'Contraseña de Admin',
        'login_as_admin': 'Iniciar Sesión como Admin',
        'admin_logged_in': '¡Admin conectado!',
        'invalid_credentials': 'Credenciales de admin inválidas',
        'full_name': 'Nombre Completo',
        'date_of_birth': 'Fecha de Nacimiento',
        'address': 'Dirección',
        'phone_number': 'Número de Teléfono',
        'email': 'Email',
        'bank_account': 'Cuenta Bancaria',
        'relationship_to_org': 'Relación con la Organización',
        'direct_beneficiary': 'Beneficiario Directo',
        'family_member': 'Miembro de la Familia',
        'description_of_need': 'Descripción de Necesidad o Apoyo',
        'declaration': 'Declaro que la información es precisa y consiento el uso de datos.',
        'register_beneficiary_btn': 'Registrar Beneficiario',
        'org_name': 'Nombre Completo / Nombre de Organización',
        'contact_person': 'Persona de Contacto (si es organización)',
        'type_of_support': 'Tipo de Apoyo',
        'financial': 'Financiero',
        'in_kind': 'En Especie',
        'volunteer': 'Voluntario',
        'other': 'Otro',
        'donation_value': 'Cantidad de Donación / Valor',
        'frequency': 'Frecuencia',
        'one_time': 'Una vez',
        'monthly': 'Mensual',
        'quarterly': 'Trimestral',
        'annually': 'Anual',
        'preferred_contact': 'Método de Contacto Preferido',
        'phone': 'Teléfono',
        'mail': 'Correo',
        'register_supporter_btn': 'Registrar Partidario',
        'reports_dashboard': '📊 Panel de Informes',
        'summary': '📌 Resumen',
        'beneficiaries': 'Beneficiarios',
        'supporters': 'Partidarios',
        'matches': 'Coincidencias',
        'download_csv': '⬇️ Descargar CSV de {table}',
        'no_records': 'No se encontraron registros de {table}.',
        'success_registered': '¡{type} registrado exitosamente!',
        'failed_register': 'Error al registrar {type}.',
        'complete_required_fields': 'Por favor complete todos los campos requeridos y acepte la declaración.',
        'invalid_email': 'Formato de email inválido.',
        'invalid_phone': 'Número de teléfono inválido.',
        'supabase_error': 'Faltan credenciales de Supabase. Ponga SUPABASE_URL y SUPABASE_KEY en un archivo .env.',
        'contact_admin': 'Contactar Admin',
        'contact_us': 'Contáctanos',
        'help_support': 'Ayuda y Soporte',
        'subject': 'Asunto',
        'message': 'Mensaje',
        'urgent': 'Urgente',
        'general_inquiry': 'Consulta General',
        'technical_issue': 'Problema Técnico',
        'registration_help': 'Ayuda de Registro',
        'data_correction': 'Corrección de Datos',
        'send_message': 'Enviar Mensaje',
        'message_sent': '¡Mensaje enviado exitosamente!',
        'message_failed': 'Error al enviar mensaje.',
        'admin_contact_info': 'Información de Contacto del Admin',
        'phone_contact': 'Contacto Telefónico',
        'email_contact': 'Contacto por Email',
        'office_hours': 'Horario de Oficina',
        'emergency_contact': 'Contacto de Emergencia',
        'faq': 'Preguntas Frecuentes',
        'how_to_register': '¿Cómo registrarse?',
        'forgot_password': '¿Olvidaste tu contraseña?',
        'update_info': '¿Cómo actualizar mi información?'
    },
    'fr': {
        'title': '🤝 BetterTogether',
        'today': "Aujourd'hui",
        'navigation': 'Navigation',
        'home': 'Accueil',
        'register_beneficiary': 'Inscrire un Bénéficiaire',
        'register_supporter': 'Inscrire un Supporter/Donateur',
        'reports': 'Rapports',
        'admin': 'Admin',
        'language': 'Langue',
        'welcome_message': 'Bienvenue sur la plateforme BetterTogether. Connectez les Bénéficiaires avec les Supporters offrant de l\'aide.',
        'system_status': 'État du Système',
        'features_disabled': 'Certaines fonctionnalités sont désactivées en raison de problèmes de base de données:',
        'admin_login': 'Connexion Admin',
        'admin_email': 'Email Admin',
        'admin_password': 'Mot de Passe Admin',
        'login_as_admin': 'Se Connecter en tant qu\'Admin',
        'admin_logged_in': 'Admin connecté!',
        'invalid_credentials': 'Identifiants admin invalides',
        'full_name': 'Nom Complet',
        'date_of_birth': 'Date de Naissance',
        'address': 'Adresse',
        'phone_number': 'Numéro de Téléphone',
        'email': 'Email',
        'bank_account': 'Compte Bancaire',
        'relationship_to_org': 'Relation avec l\'Organisation',
        'direct_beneficiary': 'Bénéficiaire Direct',
        'family_member': 'Membre de la Famille',
        'description_of_need': 'Description du Besoin ou du Support',
        'declaration': 'Je déclare que les informations sont exactes et je consens à l\'utilisation des données.',
        'register_beneficiary_btn': 'Inscrire le Bénéficiaire',
        'org_name': 'Nom Complet / Nom d\'Organisation',
        'contact_person': 'Personne de Contact (si organisation)',
        'type_of_support': 'Type de Support',
        'financial': 'Financier',
        'in_kind': 'En Nature',
        'volunteer': 'Bénévole',
        'other': 'Autre',
        'donation_value': 'Montant de Don / Valeur',
        'frequency': 'Fréquence',
        'one_time': 'Une fois',
        'monthly': 'Mensuel',
        'quarterly': 'Trimestriel',
        'annually': 'Annuel',
        'preferred_contact': 'Méthode de Contact Préférée',
        'phone': 'Téléphone',
        'mail': 'Courrier',
        'register_supporter_btn': 'Inscrire le Supporter',
        'reports_dashboard': '📊 Tableau de Bord des Rapports',
        'summary': '📌 Résumé',
        'beneficiaries': 'Bénéficiaires',
        'supporters': 'Supporters',
        'matches': 'Correspondances',
        'download_csv': '⬇️ Télécharger CSV {table}',
        'no_records': 'Aucun enregistrement de {table} trouvé.',
        'success_registered': '{type} inscrit avec succès!',
        'failed_register': 'Échec de l\'inscription de {type}.',
        'complete_required_fields': 'Veuillez remplir tous les champs obligatoires et accepter la déclaration.',
        'invalid_email': 'Format d\'email invalide.',
        'invalid_phone': 'Numéro de téléphone invalide.',
        'supabase_error': 'Identifiants Supabase manquants. Mettez SUPABASE_URL et SUPABASE_KEY dans un fichier .env.',
        'contact_admin': 'Contacter l\'Admin',
        'contact_us': 'Nous Contacter',
        'help_support': 'Aide et Support',
        'subject': 'Sujet',
        'message': 'Message',
        'urgent': 'Urgent',
        'general_inquiry': 'Demande Générale',
        'technical_issue': 'Problème Technique',
        'registration_help': 'Aide à l\'Inscription',
        'data_correction': 'Correction de Données',
        'send_message': 'Envoyer le Message',
        'message_sent': 'Message envoyé avec succès!',
        'message_failed': 'Échec de l\'envoi du message.',
        'admin_contact_info': 'Informations de Contact Admin',
        'phone_contact': 'Contact Téléphonique',
        'email_contact': 'Contact Email',
        'office_hours': 'Heures de Bureau',
        'emergency_contact': 'Contact d\'Urgence',
        'faq': 'Questions Fréquentes',
        'how_to_register': 'Comment s\'inscrire?',
        'forgot_password': 'Mot de passe oublié?',
        'update_info': 'Comment mettre à jour mes informations?'
    },
    'am': {  # Amharic
        'title': '🤝 የማህበረሰብ ማገናኛ',
        'today': 'ዛሬ',
        'navigation': 'መሄጃ',
        'home': 'ወደ ቤት',
        'register_beneficiary': 'ተጠቃሚን መመዝገብ',
        'register_supporter': 'ደጋፊ/ለጋሽ መመዝገብ',
        'reports': 'ሪፖርቶች',
        'admin': 'አስተዳዳሪ',
        'language': 'ቋንቋ',
        'welcome_message': 'ወደ የማህበረሰብ ማገናኛ መድረክ እንኳን በደህና መጡ። ተጠቃሚዎችን እርዳታ ከሚያቀርቡ ደጋፊዎች ጋር ያገናኙ።',
        'system_status': 'የስርዓት ሁኔታ',
        'features_disabled': 'በመረጃ ቋት ችግሮች ምክንያት አንዳንድ ባህሪያት ተሰናክለዋል:',
        'admin_login': 'አስተዳዳሪ መግቢያ',
        'admin_email': 'አስተዳዳሪ ኢሜይል',
        'admin_password': 'አስተዳዳሪ የይለፍ ቃል',
        'login_as_admin': 'እንደ አስተዳዳሪ ይግቡ',
        'admin_logged_in': 'አስተዳዳሪ ገብቷል!',
        'invalid_credentials': 'የተሳሳተ አስተዳዳሪ መረጃ',
        'full_name': 'ሙሉ ስም',
        'date_of_birth': 'የትውልድ ቀን',
        'address': 'አድራሻ',
        'phone_number': 'ስልክ ቁጥር',
        'email': 'ኢሜይል',
        'bank_account': 'የባንክ ሒሳብ',
        'relationship_to_org': 'ከድርጅቱ ጋር ያለው ግንኙነት',
        'direct_beneficiary': 'ቀጥተኛ ተጠቃሚ',
        'family_member': 'የቤተሰብ አባል',
        'description_of_need': 'የፍላጎት ወይም ድጋፍ መግለጫ',
        'declaration': 'መረጃው ትክክል መሆኑን አረጋግጣለሁ እና ለመረጃ አጠቃቀም እስማማለሁ።',
        'register_beneficiary_btn': 'ተጠቃሚን መመዝገብ',
        'org_name': 'ሙሉ ስም / የድርጅት ስም',
        'contact_person': 'የመገናኛ ሰው (ድርጅት ከሆነ)',
        'type_of_support': 'የድጋፍ አይነት',
        'financial': 'የገንዘብ',
        'in_kind': 'እቃ',
        'volunteer': 'በጎ ፈቃደኛ',
        'other': 'ሌላ',
        'donation_value': 'የልገሳ መጠን / ዋጋ',
        'frequency': 'ድግግሞሽ',
        'one_time': 'አንድ ጊዜ',
        'monthly': 'ወርሃዊ',
        'quarterly': 'ሩብ አመታዊ',
        'annually': 'አመታዊ',
        'preferred_contact': 'የተመረጠ የመገናኛ መንገድ',
        'phone': 'ስልክ',
        'mail': 'ፖስታ',
        'register_supporter_btn': 'ደጋፊን መመዝገብ',
        'reports_dashboard': '📊 የሪፖርቶች ዳሽቦርድ',
        'summary': '📌 خلاصة',
        'beneficiaries': 'ተጠቃሚዎች',
        'supporters': 'ደጋፊዎች',
        'matches': 'ግንኙነቶች',
        'download_csv': '⬇️ {table} CSV አውርድ',
        'no_records': 'የ{table} መዝገቦች አልተገኙም።',
        'success_registered': '{type} በተሳካ ሁኔታ ተመዝግቧል!',
        'failed_register': '{type} ማስመዝገብ አልተሳካም።',
        'complete_required_fields': 'እባክዎ ሁሉንም አስፈላጊ መስኮች ይሙሉ እና ለመግለጫው ይስማሙ።',
        'invalid_email': 'የተሳሳተ ኢሜይል ቅርፅ።',
        'invalid_phone': 'የተሳሳተ ስልክ ቁጥር።',
        'supabase_error': 'የSupabase ማረጋገጫዎች ተሰናክለዋል። SUPABASE_URL እና SUPABASE_KEY በ.env ፋይል ውስጥ ያስቀምጡ።',
        'contact_admin': 'አስተዳዳሪን ያነጋግሩ',
        'contact_us': 'ያነጋግሩን',
        'help_support': 'እርዳታ እና ድጋፍ',
        'subject': 'ርዕስ',
        'message': 'መልእክት',
        'urgent': 'አስቸኳይ',
        'general_inquiry': 'አጠቃላይ ጥያቄ',
        'technical_issue': 'ቴክኒካዊ ችግር',
        'registration_help': 'የምዝገባ እርዳታ',
        'data_correction': 'የመረጃ ማስተካከያ',
        'send_message': 'መልእክት ላክ',
        'message_sent': 'መልእክት በተሳካ ሁኔታ ተልኳል!',
        'message_failed': 'መልእክት መላክ አልተሳካም።',
        'admin_contact_info': 'የአስተዳዳሪ የእውቅና መረጃ',
        'phone_contact': 'የስልክ እውቅና',
        'email_contact': 'የኢሜይል እውቅና',
        'office_hours': 'የቢሮ ሰዓት',
        'emergency_contact': 'የአስቸኳይ እውቅና',
        'faq': 'በተደጋጋሚ የሚጠየቁ ጥያቄዎች',
        'how_to_register': 'እንዴት መመዝገብ ይቻላል?',
        'forgot_password': 'የይለፍ ቃል ረሱ?',
        'update_info': 'መረጃየን እንዴት ማዘመን እችላለሁ?'
    },
    'ti': {  # Tigrinya
        'title': '🤝 ናይ ሕብረተሰብ ማሕበር',
        'today': 'ሎሚ',
        'navigation': 'መሳገሪ',
        'home': 'ገዛ',
        'register_beneficiary': 'ተጠቃሚ ምዝገባ',
        'register_supporter': 'ደጋፊ/ዋሃቢ ምዝገባ',
        'reports': 'ሪፖርታት',
        'admin': 'ኣስተዳዳሪ',
        'language': 'ቋንቋ',
        'welcome_message': 'ናብ ናይ ሕብረተሰብ ማሕበር መድረኽ እንቋዕ ብደሓን መጻእኩም። ተጠቃማይ ምስ ሓገዛ ዚህቡ ደገፍቲ ኣሕሽሩ።',
        'system_status': 'ሓበሬታ ስርዓት',
        'features_disabled': 'ብሰበብ ናይ ዳታቤዝ ጸገማት ገለ ባህርያት ተዓጽዮም:',
        'admin_login': 'ኣስተዳዳሪ መእተዊ',
        'admin_email': 'ኣስተዳዳሪ ኢመይል',
        'admin_password': 'ኣስተዳዳሪ ምስጢር ቃል',
        'login_as_admin': 'ከም ኣስተዳዳሪ ኣቱ',
        'admin_logged_in': 'ኣስተዳዳሪ ኣቲዩ!',
        'invalid_credentials': 'ዘይቅኑዕ ናይ ኣስተዳዳሪ መረጋገጺ',
        'full_name': 'ሙሉእ ስም',
        'date_of_birth': 'ዕለት ልደት',
        'address': 'ኣድራሻ',
        'phone_number': 'ናይ ቴለፎን ቁጽሪ',
        'email': 'ኢመይል',
        'bank_account': 'ናይ ባንክ ሒሳብ',
        'relationship_to_org': 'ምስ ውዳበ ዘሎ ዝምድና',
        'direct_beneficiary': 'ቀጥተኛ ተጠቃሚ',
        'family_member': 'ናይ ስድራቤት ኣባል',
        'description_of_need': 'ናይ ድሌት ወይ ደገፍ መግለጺ',
        'declaration': 'እቲ ሓበሬታ ቅኑዕ ምዃኑን ንኣጠቓቕማ መረጃ ዚሰማምዕ ምዃነይን የረጋግጽ።',
        'register_beneficiary_btn': 'ተጠቃሚ ምዝገባ',
        'org_name': 'ሙሉእ ስም / ናይ ውዳበ ስም',
        'contact_person': 'ናይ ርክብ ሰብ (ውዳበ እንተኾይኑ)',
        'type_of_support': 'ዓይነት ደገፍ',
        'financial': 'ገንዘባዊ',
        'in_kind': 'ንብረት',
        'volunteer': 'ወላዳይነት',
        'other': 'ካልእ',
        'donation_value': 'መጠን ወይ ዋጋ ሃድነት',
        'frequency': 'ድግግምነት',
        'one_time': 'ሓደ ግዜ',
        'monthly': 'ወርሓዊ',
        'quarterly': 'ሩብዓዊ',
        'annually': 'ዓመታዊ',
        'preferred_contact': 'ዚመረጸ ናይ ርክብ ኣገባብ',
        'phone': 'ቴለፎን',
        'mail': 'ፖስታ',
        'register_supporter_btn': 'ደጋፊ ምዝገባ',
        'reports_dashboard': '📊 ናይ ሪፖርታት ዳሽቦርድ',
        'summary': '📌 ሓፂር መግለጺ',
        'beneficiaries': 'ተጠቃማይ',
        'supporters': 'ደገፍቲ',
        'matches': 'ርክባት',
        'download_csv': '⬇️ {table} CSV ኣውርድ',
        'no_records': 'ናይ {table} መዝገባት ኣይተረኽቡን።',
        'success_registered': '{type} ብዓወት ተመዝጊቡ!',
        'failed_register': '{type} ምዝገባ ኣይተሳካን።',
        'complete_required_fields': 'በጃኹም ኩሎም ኣገደስቲ መስኮታት ምልኡን ንመግለጺ ሰማምዑን።',
        'invalid_email': 'ዘይቅኑዕ ናይ ኢመይል ቅርጺ።',
        'invalid_phone': 'ዘይቅኑዕ ናይ ቴለፎን ቁጽሪ።',
        'supabase_error': 'ናይ Supabase መረጋገጺታት ጠፊኦም። SUPABASE_URL ከምኡውን SUPABASE_KEY ኣብ .env ፋይል ኣቐምጡ።'
    }
}

# -------------------------
# Translation helper function
# -------------------------
def get_text(key: str) -> str:
    """Get translated text based on current language"""
    lang = st.session_state.get('language', 'en')
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)

# -------------------------
# Load config
# -------------------------
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error(get_text('supabase_error'))
    st.stop()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(level=logging.INFO, filename='app.log')
logger = logging.getLogger(__name__)

# -------------------------
# Session state initialization
# -------------------------
for key, default in {
    "Admin_authenticated": False,
    "schema_warnings": [],
    "matches_enabled": True,
    "locks_enabled": True,
    "language": "en"
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# -------------------------
# Helper functions
# -------------------------
def insert_record(table: str, data: dict) -> bool:
    try:
        res = supabase.table(table).insert(data).execute()
        logger.info(f"Insert response: {res}")
        if hasattr(res, "data") and res.data:
            logger.info(f"Inserted record into {table}: {res.data}")
            return True
        return False
    except Exception as e:
        logger.error(f"Insert failed for {table}: {str(e)}")
        return False


def fetch_table(table: str) -> pd.DataFrame:
    try:
        res = supabase.table(table).select("*").execute()
        if hasattr(res, "data") and res.data:
            return pd.DataFrame(res.data)
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Fetch failed for {table}: {str(e)}")
        return pd.DataFrame()

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.match(r"^\+?\d{7,15}$", phone)

def mask_account(account):
    return f"****{account[-4:]}" if account else ""

# -------------------------
# Schema validation
# -------------------------
def validate_schema():
    critical_tables = [
        ("beneficiaries", {"id", "full_name", "phone_number", "status", "bank_account"}),
        ("supporters", {"id", "organization_name", "phone_number", "status"})
    ]
    optional_tables = [
        ("matches", {"beneficiary_id", "supporter_id", "matched_at"}),
        ("locks", {"lock_name", "is_locked", "locked_at"})
    ]
    warnings = []
    for table, required_cols in critical_tables + optional_tables:
        df = fetch_table(table)
        if not df.empty and not required_cols.issubset(df.columns):
            warnings.append(f"Table {table} missing required columns: {required_cols - set(df.columns)}")
            logger.warning(f"Schema warning for table {table}: {warnings[-1]}")
    st.session_state["schema_warnings"] = warnings
validate_schema()

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="BetterTogether", layout="wide")

# Language selector at the top
col1, col2 = st.columns([3, 1])
with col1:
    st.title(get_text('title'))
    st.caption(f"📅 {get_text('today')}: {datetime.today().strftime('%B %d, %Y')}")

with col2:
    language_options = {
        'en': '🇺🇸 English',
        'de': '🇩🇪 Deutsch', 
        'es': '🇪🇸 Español',
        'fr': '🇫🇷 Français',
        'am': '🇪🇹 አማርኛ',
        'ti': '🇪🇷 ትግርኛ'
    }
    
    selected_lang = st.selectbox(
        get_text('language'),
        options=list(language_options.keys()),
        format_func=lambda x: language_options[x],
        index=list(language_options.keys()).index(st.session_state.get('language', 'en'))
    )
    
    if selected_lang != st.session_state.get('language'):
        st.session_state['language'] = selected_lang
        st.rerun()

# -------------------------
# Sidebar navigation
# -------------------------
menu_options = [
    get_text('home'), 
    get_text('register_beneficiary'), 
    get_text('register_supporter'), 
    get_text('contact_us'),
    get_text('admin')
]

# Add Reports only if admin is authenticated
if st.session_state.get("Admin_authenticated", False):
    menu_options.insert(3, get_text('reports'))  # Insert before contact_us

menu = st.sidebar.radio(get_text('navigation'), menu_options)

# Add contact info in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(f"### 📞 {get_text('contact_admin')}")
st.sidebar.markdown(f"**{get_text('phone_contact')}:** +49-176-451-74080")
st.sidebar.markdown(f"**{get_text('email_contact')}:** admin@communitymatcher.org")
st.sidebar.markdown(f"**{get_text('office_hours')}:** 8:00 AM - 6:00 PM")
st.sidebar.markdown(f"**{get_text('emergency_contact')}:** +251-91-111-2222")

# -------------------------
# Admin login only on Admin page
# -------------------------
if menu == get_text('admin') and not st.session_state["Admin_authenticated"]:
    st.subheader(get_text('admin_login'))
    with st.form("admin_login_form"):
        admin_email = st.text_input(get_text('admin_email'))
        admin_password = st.text_input(get_text('admin_password'), type="password")
        admin_login_button = st.form_submit_button(get_text('login_as_admin'))
        if admin_login_button:
            if admin_email in ["hailiyekidu@gmail.com", "admin@example.com"] and admin_password == "admin123":
                st.session_state["Admin_authenticated"] = True
                st.success(get_text('admin_logged_in'))
                st.rerun()
            else:
                st.error(get_text('invalid_credentials'))
    st.stop()

# -------------------------
# Pages
# -------------------------
if menu == get_text('home'):
    st.markdown(get_text('welcome_message'))
    if st.session_state.get("schema_warnings"):
        with st.expander(get_text('system_status'), expanded=True):
            st.warning(get_text('features_disabled'))
            for warning in st.session_state["schema_warnings"]:
                st.write(f"- {warning}")
# #Beneficiary Registration Section
# elif menu == get_text('register_beneficiary'):
#     st.subheader(get_text('beneficiaries'))
#     with st.form("beneficiary_form"):
#         full_name = st.text_input(get_text('full_name'))
#         email = st.text_input(get_text('email'))
#         phone = st.text_input(get_text('phone_contact'))
#         bank_account = st.text_input("Bank Account")
#         submit = st.form_submit_button("Register Beneficiary")

#         if submit:
#             if full_name and email and phone and bank_account:
#                 if not is_valid_email(email):
#                     st.error(get_text('invalid_email'))
#                 elif not is_valid_phone(phone):
#                     st.error(get_text('invalid_phone'))
#                 else:
#                     data = {
#                         "full_name": full_name,
#                         "email": email,
#                         "phone": phone,
#                         "bank_account": bank_account,
#                         "submitted_at": datetime.now().isoformat()
#                     }
#                     if insert_record("beneficiaries", data):
#                         st.success("Beneficiary registered successfully.")
#                     else:
#                         st.error("Failed to register Beneficiary.")
#             else:
#                 st.error(get_text('complete_required_fields'))

#     # Supporter Registration Section
# elif menu == get_text('register_supporter'):
#     st.subheader(get_text('supporters'))
#     with st.form("supporter_form"):
#         full_name = st.text_input(get_text('full_name'))
#         email = st.text_input(get_text('email'))
#         phone = st.text_input(get_text('phone_contact'))
#         submit = st.form_submit_button("Register Supporter")

#         if submit:
#             if full_name and email and phone:
#                 if not is_valid_email(email):
#                     st.error(get_text('invalid_email'))
#                 elif not is_valid_phone(phone):
#                     st.error(get_text('invalid_phone'))
#                 else:
#                     data = {
#                         "full_name": full_name,
#                         "email": email,
#                         "phone": phone,
#                         "submitted_at": datetime.now().isoformat()
#                     }
#                     if insert_record("supporters", data):
#                         st.success("Supporter registered successfully.")
#                     else:
#                         st.error("Failed to register Supporter.")
#             else:
#                 st.error(get_text('complete_required_fields'))

elif menu == get_text('register_beneficiary'):
    st.subheader(get_text('register_beneficiary'))
    with st.form("beneficiary_form"):
        full_name = st.text_input(get_text('full_name'))
        dob = st.date_input(get_text('date_of_birth'))
        address = st.text_area(get_text('address'))
        phone = st.text_input(get_text('phone_number'))
        email = st.text_input(get_text('email'))
        bank_account = st.text_input(get_text('bank_account'))
        relationship = st.selectbox(get_text('relationship_to_org'), [get_text('direct_beneficiary'), get_text('family_member')])
        description = st.text_area(get_text('description_of_need'))
        declaration = st.checkbox(get_text('declaration'))
        submit = st.form_submit_button(get_text('register_beneficiary_btn'))
        if submit:
            if full_name and phone and declaration:
                if email and not is_valid_email(email):
                    st.error(get_text('invalid_email'))
                elif not is_valid_phone(phone):
                    st.error(get_text('invalid_phone'))
                else:
                    data = {
                        "full_name": full_name,
                        "date_of_birth": dob.strftime("%Y-%m-%d"),
                        "address": address,
                        "phone_number": phone,
                        "email": email,
                        "bank_account": bank_account,
                        "relationship_to_org": relationship,
                        "description_of_need": description,
                        "declaration_consent": True,
                        "submitted_at": datetime.now().isoformat(),
                        "status": "Pending"
                    }
                    if insert_record("beneficiaries", data):
                        st.success(get_text('success_registered').format(type=get_text('beneficiaries')))
                    else:
                        st.error(get_text('failed_register').format(type=get_text('beneficiaries')))
            else:
                st.error(get_text('complete_required_fields'))

elif menu == get_text('register_supporter'):
    st.subheader(get_text('register_supporter'))
    with st.form("supporter_form"):
        org_name = st.text_input(get_text('org_name'))
        contact_person = st.text_input(get_text('contact_person'))
        address = st.text_area(get_text('address'))
        phone = st.text_input(get_text('phone_number'))
        email = st.text_input(get_text('email'))
        support_type = st.multiselect(get_text('type_of_support'), [
            get_text('financial'), 
            get_text('in_kind'), 
            get_text('volunteer'), 
            get_text('other')
        ])
        donation_value = st.text_input(get_text('donation_value'))
        frequency = st.selectbox(get_text('frequency'), [
            get_text('one_time'), 
            get_text('monthly'), 
            get_text('quarterly'), 
            get_text('annually')
        ])
        preferred_contact = st.selectbox(get_text('preferred_contact'), [
            get_text('email'), 
            get_text('phone'), 
            get_text('mail')
        ])
        declaration = st.checkbox(get_text('declaration'))
        submit = st.form_submit_button(get_text('register_supporter_btn'))
        if submit:
            if org_name and phone and declaration:
                if email and not is_valid_email(email):
                    st.error(get_text('invalid_email'))
                elif not is_valid_phone(phone):
                    st.error(get_text('invalid_phone'))
                else:
                    data = {
                        "organization_name": org_name,
                        "contact_person": contact_person,
                        "address": address,
                        "phone_number": phone,
                        "email": email,
                        "type_of_support": ", ".join(support_type),
                        "donation_value": donation_value,
                        "frequency": frequency,
                        "preferred_contact": preferred_contact,
                        "declaration_consent": True,
                        "submitted_at": datetime.now().isoformat(),
                        "status": "Pending"
                    }
                    if insert_record("supporters", data):
                        st.success(get_text('success_registered').format(type=get_text('supporters')))
                    else:
                        st.error(get_text('failed_register').format(type=get_text('supporters')))
            else:
                st.error(get_text('complete_required_fields'))
#Contact Us Section
elif menu == get_text('contact_us'):
    st.subheader(get_text('contact_us'))
    with st.form("contact_form"):
        subject = st.selectbox(get_text('subject'), [
            get_text('urgent'),
            get_text('general_inquiry'),
            get_text('technical_issue'),
            get_text('registration_help'),
            get_text('data_correction')
        ])
        message = st.text_area(get_text('message'))
        send_button = st.form_submit_button(get_text('send_message'))

        if send_button:
            if message:
                # Here you would typically send the message to an email or store it in a database
                st.success(get_text('message_sent'))
            else:
                st.error(get_text('complete_required_fields'))
##########Reports Section##########

elif menu == get_text('reports'):
    if not st.session_state.get("Admin_authenticated", False):
        st.warning(get_text("admin_login") + " " + get_text("required_to_access"))
        st.stop()

    st.subheader(get_text('reports_dashboard'))

    # Fetch data
    b_df = fetch_table("beneficiaries")
    s_df = fetch_table("supporters")
    m_df = fetch_table("matches")

    # Mask bank accounts
    if not b_df.empty and "bank_account" in b_df.columns:
        b_df["bank_account"] = b_df["bank_account"].apply(mask_account)

    # Summary Section
    st.markdown("## 📊 " + get_text('summary'))
    col1, col2, col3 = st.columns(3)
    col1.metric(get_text('beneficiaries'), len(b_df))
    col2.metric(get_text('supporters'), len(s_df))
    col3.metric(get_text('matches'), len(m_df))

    st.markdown("---")

    # Beneficiaries Section
    st.markdown("## 🧍 " + get_text('beneficiaries'))
    if not b_df.empty:
        st.dataframe(b_df, use_container_width=True)
        st.download_button(
            label=get_text('download_csv').format(table=get_text('beneficiaries')),
            data=b_df.to_csv(index=False),
            file_name="beneficiaries.csv"
        )
    else:
        st.info(get_text('no_records').format(table=get_text('beneficiaries').lower()))

    st.markdown("---")

    # Supporters Section
    st.markdown("## 🤝 " + get_text('supporters'))
    if not s_df.empty:
        st.dataframe(s_df, use_container_width=True)
        st.download_button(
            label=get_text('download_csv').format(table=get_text('supporters')),
            data=s_df.to_csv(index=False),
            file_name="supporters.csv"
        )
    else:
        st.info(get_text('no_records').format(table=get_text('supporters').lower()))

    st.markdown("---")

    # Matches Section
    st.markdown("## 🔗 " + get_text('matches'))
    if st.session_state.get("matches_enabled", True):
        if not m_df.empty:
            st.dataframe(m_df, use_container_width=True)
            st.download_button(
                label=get_text('download_csv').format(table=get_text('matches')),
                data=m_df.to_csv(index=False),
                file_name="matches.csv"
            )
        else:
            st.info(get_text('no_records').format(table=get_text('matches').lower()))
