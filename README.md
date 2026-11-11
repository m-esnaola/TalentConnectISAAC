# TalentConnect - ISAAC

## ¿De qué trata el proyecto?

**TalentConnect** es un proyecto educativo de CEBANC orientado a conectar personas que buscan empleo en el sector tecnológico con ofertas de trabajo. Combina una **página web** para consultar información y enviar un CV con un **programa en Python** para gestionar candidatos, ofertas y procesos de selección.

## Objetivos
- Mostrar ofertas de empleo y facilitar el envío de candidaturas mediante un formulario HTML.
- Registrar y consultar candidatos, ofertas y estados de las candidaturas.
- Practicar **HTML, CSS, JavaScript, Python, JSON y Git/GitHub** trabajando en equipo.

## Reparto del trabajo
| Apartado | Responsable |
| --- | --- |
| Pagina Principal (`talentConnect.html`) y su CSS | **Maitane** |
| Formulario (`formulario.html`) y estilos | **Ares, Claudia e Ibon** |
| Validación con JavaScript (`scripts/validar.js`) | **Ares, Claudia e Ibon** |
| Gestión de candidatos (`candidatos.py`) | **Claudia, Ibon, Ares y Maitane** |
| Consulta de ofertas (`ofertas.py`) | **Maitane** |
| Procesos de selección (`procesos_seleccion.py`) | **Ares** |
| Gestion de usuarios (`usuario.py`) | **Maitane** |
| Main (`main.py`) | **Todos los integrantes (Ares, Ibon, Claudia y Maitane)** |

## Cómo utilizarlo
1. Descarga o clona el repositorio y abre la carpeta en **Visual Studio Code**.
2. Para ver la web, abre `talentConnect.html` en el navegador. El botón **Enviar CV** lleva al formulario.
3. Para ejecutar el programa de gestión, abre una terminal en la carpeta del proyecto y escribe:

```bash
python main.py
```
4. Desde el menú puedes iniciar sesión o crear una cuenta y tras ello, acceder a la gestión de candidatos, ofertas y procesos de selección. Los datos se guardan en archivos **JSON**.

## Herramientas y trabajo en equipo
Se ha usado **Git y GitHub** para trabajar mediante ramas, realizar commits y fusionar cambios (*merge*). Los conflictos se han resuelto con el editor de VS Code.

**Repositorio:** https://github.com/m-esnaola/TalentConnectISAAC

*Imagen de la pagina principal*
![Pagina Principal de TalentConnect](https://res.cloudinary.com/bq6uwaym/image/upload/v1794302746/Captura_de_pantalla_2026-11-10_102406.png)

*Imagen del formulario*
![Pagina del formulario de TalentConnect](https://res.cloudinary.com/bq6uwaym/image/upload/v1794302847/Captura_de_pantalla_2026-11-10_102647.png)
