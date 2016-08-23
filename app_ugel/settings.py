# -*- encoding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^6iyl8-t#d+azlyf(ph^)y2f76!11i!-%8-=#ngf-#j!xbgc8+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #APP
    'estudios_realizados.apps.EstudiosRealizadosConfig',
    'cursos_capacitaciones_pedagogicos.apps.CursosCapacitacionesPedagogicosConfig',
    'formaciones_capacitaciones_cargos.apps.FormacionesCapacitacionesCargosConfig',
    'experiencias_sector_educativos.apps.ExperienciasSectorEducativosConfig',
    'experiencias_trabajos_aulas.apps.ExperienciasTrabajosAulasConfig',
    'experiencias_docentes.apps.ExperienciasDocentesConfig',
    'experiencias_asesorias_acompanamientos_pedagogicos.apps.ExperienciasAsesoriasAcompanamientosPedagogicosConfig',
    'experiencias_procesos_capacitaciones_formaciones.apps.ExperienciasProcesosCapacitacionesFormacionesConfig',
    'evaluaciones.apps.EvaluacionesConfig',
    #'preguntas.apps.PreguntasConfig',
    #'alternativas.apps.AlternativasConfig',
    #'cuestionarios.apps.CuestionariosConfig',
    #INDEX 
    'index.apps.IndexConfig',
    'menus.apps.MenusConfig',
    'grupos_menus.apps.GruposMenusConfig',
    #DOCENTES
    'clases_entidades.apps.ClasesEntidadesConfig',
    'tipos_entidades.apps.TiposEntidadesConfig',
    'entidades.apps.EntidadesConfig',
    'usuarios.apps.UsuariosConfig',
    'docentes.apps.DocentesConfig',
    'documentos_identificaciones.apps.DocumentosIdentificacionesConfig',
    'tipos_personas.apps.TiposPersonasConfig',
    'tipos_docentes.apps.TiposDocentesConfig',
    'estados_civiles.apps.EstadosCivilesConfig',
    'grupos_sanguineos.apps.GruposSanguineosConfig',
    'grados_instrucciones.apps.GradosInstruccionesConfig',
    'profesiones.apps.ProfesionesConfig',
    'ocupaciones.apps.OcupacionesConfig',
    'cargos.apps.CargosConfig',
    'idiomas.apps.IdiomasConfig',
    #DIRECCION
    'vias.apps.ViasConfig',
    'zonas.apps.ZonasConfig',
    'distritos.apps.DistritosConfig',
    'provincias.apps.ProvinciasConfig',
    'departamentos.apps.DepartamentosConfig',
    'paises.apps.PaisesConfig',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_ugel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__) , 'templates').replace('\\','/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app_ugel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': "sql_server.pyodbc",
       'HOST': "127.0.0.1",
       'PORT': '1433',
       'USER': "sa",
       'PASSWORD': "S1st3mas",
       'NAME': "App_ERP",
       'OPTIONS': {
            'host_is_server': True,
        },
   }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
#Configuración de archivos estaticos 
STATIC_URL = '/static/'
#MEDIA -> STATIC
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

STATICFILES_FINDERS = {
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
}

#Activar cache para archivos estaticos
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFileStorage'

#Imagenes, audios y videos
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL  = '/media/'

#Configuración de Usuario 
AUTH_USER_MODEL = 'usuarios.Usuario'

EMAIL_HOST =  'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'victor.luis.marcelo@gmail.com'
EMAIL_HOST_PASSWORD = 'S1st3mas'
EMAIL_USE_TLS = True