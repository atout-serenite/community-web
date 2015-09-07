![valeureux](http://i.imgur.com/jbF9soZ.png)

WeZer Exchange is an open source cooperation platform built to make businesses and communities more effective. It is a product of Valeureux, “The Factory of Common goods Wealth Actualisation Tools”, which is studying, designing and teaching for many years about cooperation and sharing value.

As a software product, WeZer aims to bring many tools normally found separately into one environment, where they will be more effective, more integrated, and easier to use. As a platform, and a distribution of Odoo (ex Open ERP), anyone is invited to contribute plugins. As a tool, WeZer supports the latest thinking in organisational management and collective intelligence. WeZer is more than a tool, it’s a full device composed by a web app, an ‘implementation journey’, a community and a research program. WeZer is a systemic solution to boost cooperation, to dynamise the We!

![valeureux-wezer-mkp](http://i.imgur.com/0z42XFi.png)


More information about the platform on http://wezer.org

On wezer.org you can post your announcement and share your development proposition through our dedicated forum: https://www.wezer.org/forum/technical-development-5/

You can read our technical forum: https://www.wezer.org/forum/help-1

You can also look at English users Q&A: https://www.wezer.org/forum/english-user-q-a-2

More information about valeureux on http://valeureux.org

The OCA Communities Verticalizations project is a collaborative effort to develop a robust, commercial-grade, set of apps to transform odoo into a full featured platform for communities. 
The project is managed by a growing worldwide community of volunteers that are willing to contribute to the development and documentation to make this vision real.

## Contributing ##
If you are interested by this project, please join wezer.org platform and look at contribute pages

**Translations:**<br>Please use pot files and make pull request to repo

**Temporary process:**<br>
Currently we have a dozen of modules to include in the OCA repo which are not reviewed yet. Reviewing it will take time and we can't stop develop on them during that time. Theses modules still be in the "__unreviewed__" directory and must not be already considered OCA quality. The modules will be reviewed one by one, when a module is ready to be reviewed it will be pushed out of "__unreviewed__" directory through a merge request. 

# Installation #
Installation process is at present stage only possible in manual way. All is discribed in wezer.org forum: <br>
https://www.wezer.org/forum/help-1/question/how-to-install-wezer-on-your-server-or-vmware-30
<br>
Howevever find under some recommandations
## Prerequisite ##
Before installing the module make sure that the you have configured an addon path for custom addons. In a Linux system the parameter in the config file usually looks similar as the following example: specify additional addons paths (separated by commas)
addons_path = /opt/odoo/odoo-server/addons, /opt/odoo/custom/addons

In this case you have to install the modules into /opt/odoo/custom/addons. At the present stage on dependency could not automatically resolved so you have to install one extra module that vertical community depends on. This module is available from the Github repositories.

git clone https://github.com/OCA/account-financial-tools.git
<br>
git clone http://github.com/ingadhoc/odoo-addons.git
<br><br>

## Installing the modules ##
Then go to you odoo webinterface to the module section and start "Update module list". 
<br>
First look for the "Odoo for Communities" and the marketplace module and install them.
If you need website interface then install "Wezer dependencies" module

Back-end cames from OCA-vertical community repo
<br> and website was old community-web repo


