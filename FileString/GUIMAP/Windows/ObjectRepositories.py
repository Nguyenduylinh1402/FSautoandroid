"""
@Company: FileString
@Author: minh.nguyen
@Date: Sept 22, 2014
@Description: store all object repositories in FileString desktop application
@Last update: October 9, 2014

===================Template====================
'''
@Author: user
@Date: N/A
@Description: N/A
@Last update: N/A
'''
or more simple
# this is guimap description
gmwin_exampleVariable=[
	# 0 | This is description of this element
	"//this_is_element_locator[@type='an_id']" 
]

# description
name=[
	# 0 | 
	"",
	# 1 | 
	"",
	# 2 | 
	"",
	# 3 | 
	"",
	# 4 | 
	"",
	# 5 | 
	"",
	# 6 | 
	"",
	# 7 | 
	"",
	# 8 | 
	"",
	# 9 | 
	"",
	# 10 | 
	"",
	# 11 | 
	"",
	# 12 | 
	"",
	# 13 | 
	"",
	# 14 | 
	"",
	# 15 | 
	"",
	# 16 | 
	"",
	# 17 | 
	"",
]


"""


prefix_container="/container"
prefix_form="/form"
prefix_contextMenu="/contextmenu"


# The below list contains all elements of sign in screen
gmwin_signInScreen=[
	# 0 | Sign in screen
	prefix_container+"[@name='FileString Setup']",
	# 1 | FileString logo
	prefix_container+"[@name='FileString Setup']/picture[@classname='Image']",
	# 2 | Sign In text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignIn']/text",
	# 3 | Enter the email address and password for your FileString account text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignIn']/text[2]",
	# 4 | Email Address text field
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignIn']/text[@automationid='tbEmailSignIn']",
	# 5 | Password text field
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignIn']/text[@automationid='tbPasswordSignIn']",
	# 6 | link Need Help?
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignIn']/text[@automationid='tblNeedHelp']",
	# 7 | link Create a FileString Account
	prefix_container+"[@name='FileString Setup']/text[@automationid='txtSignUp']",
	# 8 | button Sign In
	prefix_container+"[@name='FileString Setup']/button[@automationid='btnNext']",
	# 9 | error message
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignIn']/text[@automationid='lbErrSignin']"
]


gmwin_windowsForm=[
	# 0 | Top left logo icon
	prefix_container+"[@name='FileString Setup']/titlebar[@automationid='TitleBar']/?/?/menuitem[@automationid='Item 1']",
	# 1 | Title bar
	prefix_container+"[@name='FileString Setup']/titlebar[@automationid='TitleBar']",
	# 2 | Minimize button
	prefix_container+"[@name='FileString Setup']/?/?/button[@automationid='Minimize']",
	# 3 | Maximize button
	prefix_container+"[@name='FileString Setup']/?/?/button[@automationid='Maximize']",
	# 4 | Close button
	prefix_container+"[@name='FileString Setup']/?/?/button[@automationid='Close']",
	# 5 | Restriction windows pop-up
	prefix_container+"[@title='Restrictions']/?/?/element[@instance='0']/button[@text='OK']"
]


gmwin_thisPCFolder=[
	# 0 | Close button
	"/form[@title='This PC']/?/?/button[@automationid='Close']"
]


gmwin_signUpScreen=[
	# 0 | Create an Account text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[1]",
	# 1 | Description text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@classname='TextBlock'][2]",
	# 2 | First Name
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@automationid='tbFirstName']",
	# 3 | Last Name
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@automationid='tbLastName']",
	# 4 | Email Address
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@automationid='tbEmailSignUp']",
	# 5 | Password
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@automationid='tbPasswordSignUp']",
	# 6 | check box
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/checkbox[@automationid='chkAgree']",
	# 7 | Text after check box
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/?/checkbox/text[1]",
	# 8 | link Terms of Service
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@automationid='tblTermOfService']",
	# 9 | button Back
	prefix_container+"[@name='FileString Setup']/button[@automationid='btnBack']",
	# 10 | button Sign Up
	prefix_container+"[@name='FileString Setup']/button[@automationid='btnNext']",
	# 11 | Error message at Sign Up screen
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabSignUp']/text[@automationid='lbErrorSignUp']/text"
]




gmwin_verifyEmailAddressScreen=[
	# 0 | Verify Your Email Address text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabVerify']/text[1]",
	# 1 | Please check your email inbox for a message from FileString and click the link to verify your email address.
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabVerify']/text[2]",
	# 2 | Back button
	prefix_container+"[@name='FileString Setup']/button[@automationid='btnBack']",
	# 3 | Continue button
	prefix_container+"[@name='FileString Setup']/button[@automationid='btnNext']",
	# 4 | Need verify text error message
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabVerify']/text[@automationid='txtNeedVerify']"
]






gmwin_congratulationScreen=[
	# 0 | Congratulations text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/text[@name='Congratulations!']",
	# 1 | You are ready to use FileString...What next? text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/text[2]",
	# 2 | Radio button take a tour
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/radiobutton[@automationid='radTour']",
	# 3 | Take a tour of FileString text
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/?/?/text",
	# 4 | Radio button Open received files...
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/radiobutton[@automationid='radOpenReceiveFolder']",
	# 5 | text Open received files...
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/radiobutton[@automationid='radOpenReceiveFolder']/text",
	# 6 | checkbox header
	# prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/table[@automationid='dataGridFiles']//checkbox[@automationid='chkHeader']",
	prefix_container+"[@name='FileString Setup']//table[@automationid='dataGridFiles']/row[@automationid='PART_ColumnHeadersPresenter']/?/?/checkbox[@automationid='chkHeader']",
	# 7 | File name header
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/table[@automationid='dataGridFiles']/?/?/cell[@name='FILE NAME']",
	# 8 | Type header
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/table[@automationid='dataGridFiles']/?/?/cell[@name='TYPE']",
	# 9 | Sender header
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/table[@automationid='dataGridFiles']/?/?/cell[@name='SENDER']",
	# 10 | Text no received files
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/text[@automationid='txtNoFiles']",
	# 11 | Next buttonhoan
	prefix_container+"[@name='FileString Setup']/button[@automationid='btnNext']",
	# 12 | No received file
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/text[@automationid='txtNoFiles']",
	# 13 | Downloading received files...
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/text[3]",
	# 14 | Progress bar
	prefix_container+"[@name='FileString Setup']/?/?/tabpage[@automationid='tabCongrats']/progressbar[@automationid='processBarDownloading']",
	# 15 | checkbox select file
	prefix_container+"[@name='FileString Setup']/?/?/table[@automationid='dataGridFiles']/row[<<index>>]/?/?/checkbox[@automationid='IsSelected']"
]


gmwin_systemTray=[
	# 0 | FileString at system tray
	"/menubar[@class='Shell_TrayWnd']/?/?/container/toolbar[@controlid='1504']/button[@text~'FileString ']",
	
]


gmwin_menuFromTrayIcon=[
	# 0 | Menu from tray icon
	prefix_form+"[@name='TrayIconMenuWindow']",
	# 1 | Logo FileString in top left of menu bar
	prefix_form+"[@name='TrayIconMenuWindow']/picture[@classname='Image']",
	# 2 | FileString version
	prefix_form+"[@name='TrayIconMenuWindow']/text[@automationid='txtVersionFS']",
	# 3 | button setting
	prefix_form+"[@name='TrayIconMenuWindow']/button[@automationid='btnSetting']",
	# 4 | Synced 
	prefix_form+"[@name='TrayIconMenuWindow']/text[@name~'Synced']",
	# 5 | Menu Recent Sent Files
	prefix_form+"[@name='TrayIconMenuWindow']/?/?/menuitem[@automationid='menuRecentSentFiles']",
	# 6 | Menu Recent Received Files
	prefix_form+"[@name='TrayIconMenuWindow']/?/?/menuitem[@automationid='menuRecentReceivedFiles']",
	# 7 | FileString Folder
	prefix_form+"[@name='TrayIconMenuWindow']/button[@automationid='FileStringFolder']",
	# 8 | FileString website
	prefix_form+"[@name='TrayIconMenuWindow']/button[5]",
	# 9 | Checking
	prefix_form+"[@name='TrayIconMenuWindow']/text[@name='Checking...']",
	# 10 | Being Synced
	prefix_form+"[@name='TrayIconMenuWindow']/text[@name~'^Synced\ ']",
	# 11 |
	"",
]



gmwin_contextMenuFromSettingButton=[
	# 0 | context menu form
	prefix_contextMenu+"[@classname='ContextMenu']",
	# 1 | Account firstname, lastname, email address (NOT DETECTED YET)
	"",
	# 2 | Device Settings
	prefix_contextMenu+"[@classname='ContextMenu']/?/?/menuitem[@name='Device Settings']",
	# 3 | Your Preferences
	prefix_contextMenu+"[@classname='ContextMenu']/?/?/menuitem[@name='Your Preferences']",
	# 4 | Help Center
	prefix_contextMenu+"[@classname='ContextMenu']/?/?/menuitem[@name='Help Center']",
	# 5 | FileString Tour
	prefix_contextMenu+"[@classname='ContextMenu']/?/?/menuitem[@name='FileString Tour']",
	# 6 | Quit FileString
	prefix_contextMenu+"[@classname='ContextMenu']/?/?/menuitem[@name='Quit FileString']",
]


gmwin_deviceSettings=[
	# 0 | Device settings form
	prefix_form+"[@name='Device Settings']",
	# 1 | Your Account text
	prefix_form+"[@name='Device Settings']/text[1]",
	# 2 | <Firstname Lastname (Email Address)> ex: Test Hau Hoang93 (hoanghau93@gmail.com)
	prefix_form+"[@name='Device Settings']/text[@automationid='txtAccountName']",
	# 3 | Computer Name text
	prefix_form+"[@name='Device Settings']/text[2]",
	# 4 | <Computer name> ex: FS-QC-DKT08
	prefix_form+"[@name='Device Settings']/text[@automationid='txtComputerName']",
	# 5 | Unlink button
	prefix_form+"[@name='Device Settings']/button[@automationid='btnUnlink']",
	# 6 | Folder Location text
	prefix_form+"[@name='Device Settings']/text[5]",
	# 7 | FileString location
	prefix_form+"[@name='Device Settings']/text[@automationid='txtFilestringLocation']",
	# 8 | Browse... button
	prefix_form+"[@name='Device Settings']/button[@automationid='btnBrowse']",
	# 9 | Start File String on system startup checkbox
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkStartUp']",
	# 10 | Start File String on system startup text
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkStartUp']/text",
	# 11 | Allow FileString to access your contacts checkbox
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkAccessContact']",
	# 12 | Allow FileString to access your contacts text
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkAccessContact']/text",
	# 13 | Show desktop notifications checkbox
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkShowdesktopNotify']",
	# 14 | Show desktop notifications text
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkShowdesktopNotify']/text",
	# 15 | Show the FileString tour each time a received file is closed checkbox
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkShowFSTour']",
	# 16 | Show the FileString tour each time a received file is closed text
	prefix_form+"[@name='Device Settings']/checkbox[@automationid='chkShowFSTour']/text",
	# 17 | OK button
	prefix_form+"[@name='Device Settings']/button[@automationid='btnOK']",
	# 18 | Cancel button
	prefix_form+"[@name='Device Settings']/button[@automationid='btnCancel']"
]



gmwin_afterClickUnlinkThisComputerButton=[
	# 0 | Form
	"/form[@name='FileString']",
	# 1 | Logo FileString
	"/form[@name='FileString']/picture[@classname='Image']",
	# 2 | text message
	"/form[@name='FileString']/text[@automationid='txtMessage']",
	# 3 | Yes button
	"/form[@name='FileString']/button[@automationid='btnOption1']",
	# 4 | No button
	"/form[@name='FileString']/button[@automationid='btnOption2']"
]


gwin_fileStringFolder=[
	# 0 | FileString folder
	"/form[@title='FileString']",
	# 1 | Close button
	"/form[@title='FileString']/?/?/button[@automationid='Close']",
	# 2 | Maximize-Restore icon
	"/form[@title='FileString']/?/?/button[@automationid='Maximize-Restore']",
	# 3 | Menu View
	"/form[@title='FileString']/element[3]//tabpagelist[@accessiblename='Ribbon tabs']/container[@accessiblename='']/tabpage[@accessiblename='View']",
	# 4 | Detail View 64 bit
	"/form[@processname='explorer' and @class='Net UI Tool Window']//container[@accessiblename='View']/toolbar[@accessiblename='Layout']/container[@accessiblename='Views']/list[@accessiblename='Views']/?/?/listitem[@accessiblename='Details']",
	#"/form[@title='FileString']/element[3]//container[@accessiblename='Lower Ribbon']/?/?/container[@accessiblename='View']/toolbar[@accessiblename='Layout']/container[@accessiblename='Views']/list[@accessiblename='Views']/?/?/listitem[@accessiblename='Details']",
	# 5 | Filename extensions
	"/form[@processname='explorer' and @class='Net UI Tool Window']//container[@accessiblename='View']/toolbar[@accessiblename='Show/hide']/checkbox[@accessiblename='File name extensions']",
	# 6 | FileSelected
	"/form[@title='FileString']/element[@class='ShellTabWindowClass']//container[@caption='ShellView']/?/?/listitem[@automationid='<<index>>']"
]


gmwin_contextMenuWhenRightClick=[
	# 0 | FileString Menu
	"/contextmenu[@class='#32768' and @instance='0']/?/?/menuitem[@accessiblename='FileString']",
	# 1 |  String this file item
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='String this File']",
	# 2 | Delete button
	"/contextmenu[@processname='explorer']/?/?/menuitem[@accessiblename='Delete']",
	# 3 | 
	"",
	# 4 | 
	"",
	# 5 | 
	"",
	# 6 | 
	"",
	# Main menu
	#      Child menu
	# 7 | File Type Not Supported
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='(File Type Not Supported)']",
	# 8 | View Supported File Formats
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename~'^View\ Supported\ File\ Forma']",
	# 9 | Copy to FileString Folder and Share
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename~'^Copy\ to\ FileString\ Folder']",
	# 10 | Move to FileString Folder and Share
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename~'^Move\ to\ FileString\ Folder']",
	# 11 | Add new recipients 
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Add new Recipients']",
	# 12 | Change Recipient Rights
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Change Recipient Rights']",
	# 13 | View Recipients
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='View Recipients']",
	# 14 | Track File Views
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Track File Views']",
	# 15 | Revoke recipient access
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Revoke Recipient Access']",
	# 16 | File Infomation
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='File Information']",
	# 17 | Show on FileString.com
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Show on FileString.com']",
	# 18 | Push file update
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Push File Update']",
	# 19 | 
	"",
	# 20 | 
	"",
]



gmwin_pdfTronIsDownPopup=[
	# 0 | Form
	"/form[@name='FileString']",
	# 1 | Image
	"/form[@name='FileString']/picture[@classname='Image']",
	# 2 | Due to system maintenance, there might be a temporary delay in delivering Microsoft Office files to your recipients. We apologize for this inconvenience. text
	"/form[@name='FileString']/text[@name~'^Due\ to\ system\ maintenance']",
	# 3 | For fast delivery of your content, convert this file to PDF and string it instead. text
	"/form[@name='FileString']/text[@name~'^For\ fast\ delivery\ of\ your']",
	# 4 | button cancel
	"/form[@name='FileString']/button[@automationid='btnCancel']",
	# 5 | button Continue
	"/form[@name='FileString']/button[@automationid='btnContinue']"

]




# this popup appear after user click on String A file if this file has extension is ppt or pptx
gmwin_shareFilePowerPointWarningPopup=[
	# 0 | FileString logo
	"/form[@name='Warning']/picture[@classname='Image']",
	# 1 | text message
	"/form[@name='Warning']/text[@automationid='tblCaption']",
	# 2 | Do not display again check box
	"/form[@name='Warning']/checkbox[@automationid='chkNotDisplayMsg']",
	# 3 | Do not display again text
	"/form[@name='Warning']/?/?/text[1]",
	# 4 | Continue button
	"/form[@name='Warning']/button[@automationid='btnConform']"
]


gmwin_notificationWhenSentFileSuccessfully=[
	# 0 | Pop-up
	"/form[@classname='Popup']/?/?/element[@classname='NoificationCustomUserControl']",
	# 1 | Filestring logo
	"/form[@classname='Popup']/element[@automationid='me']/element/picture[1]",
	# 2 | "TCs List.xl..." sent successfully
	"/form[@classname='Popup']/element[@automationid='me']/?/?/text[@automationid='txtTitle']",
	# 3 | 	
	"/form[@classname='Popup']/element[@automationid='me']/?/?/text[@automationid='txtMessage']",
	# 4 | 
	"",
	# 5 | was successfully sent to your recipients.
	"",
	# 6 | 
	"",
	# 7 | 
	"",
	# 8 | 
	"",
]

gmwin_errorMessageShareFile=[
	# 0 | Error Message Form
	"/form[@name='FileString']",
	# 1 | error message
	"/form[@name='FileString']/text[@automationid='txtMessage']",
	# 2 | OK button
	"/form[@name='FileString']/button[@automationid='btnOK']",
]

gmwin_errorMessageWithFilenameTooLong=[
	# 0 | Error message form
	"/form[@automationid='Window']",
	# 1 | Error message text
	"/form[@automationid='Window']/text[@automationid='txtMessage']",
	# 2 | Button OK
	"/form[@automationid='Window']/button[@automationid='btnOK']",
]


gmwin_revokePopup=[
	# 0 | Logo FileString
	"/form[@name='FileString']/picture[@classname='Image']",
	# 1 | text message
	"/form[@name='FileString']/text[@automationid='txtMessage']",
	# 2 | Revoke button
	"/form[@name='FileString']/button[@automationid='btnOption1']",
	# 3 | Cancel button
	"/form[@name='FileString']/button[@automationid='btnOption2']"
]

# the below elements are in Send a File popup after click String this file
gmwin_sendAFilePopup=[
	# 0 | String a File text
	"/container[@name='Send a File']/text[1]",
	# 1 | filename
	"/container[@name='Send a File']/text[@automationid='txtFileName']",
	# 2 | Recipients: text
	"/container[@name='Send a File']/text[3]",
	# 3 | email address text field
	"/container[@name='Send a File']/text[@automationid='tagBox']",
	# 4 | Show more button
	"/container[@name='Send a File']/button[@automationid='tgShowMore']",
	# 5 | Send button
	"/container[@name='Send a File']/button[@automationid='btnSend']",
	# 6 | Cancel button
	"/container[@name='Send a File']/button[@automationid='btnCancel']",
	# 7 | Display watermark checkbox
	"/container[@name='Send a File']/checkbox[@automationid='chkWatermark']",
	# 8 | 
	"",
	# 9 | 
	"",
	# 10 | 
	"",
	# 11 | 
	"",
	# 12 | 
	"",
	# 13 | 
	"",
]


gmwin_fileInformationPopup=[
	# 0 | Form
	"/form[@name='File Information']",
	# 1 | File name text
	"/form[@name='File Information']/text[@automationid='txtFileName']",
	# 2 | Logo
	"/form[@name='File Information']/picture[@classname='Image']",
	# 3 | View report button
	"/form[@name='File Information']/button[@automationid='btnTrackView']",
	# 4 | Push Update button
	"/form[@name='File Information']/button[@automationid='btnPushUpdate']",
	# 5 | View recipients button
	"/form[@name='File Information']/button[@automationid='btnViewRecipient']",
	# 6 | Add recipients button
	"/form[@name='File Information']/button[@automationid='btnAddRecipient']",
	# 7 | Revoke All button
	"/form[@name='File Information']/button[@automationid='btnRevokeAll']",
	# 8 | Close button
	"/form[@name='File Information']/button[@name='Close']",
	# 9 | List of recipients
	"/form[@name='File Information']/table[@automationid='dgRecipient']/row[<<index>>]//text",
	# 10 | File type
	"/form[@name='File Information']/text[@automationid='txtOwnerType']",
	# 11 | File size
	"/form[@name='File Information']/text[@automationid='txtOwnerSize']",
	# 12 | Pages
	"/form[@name='File Information']/text[@automationid='txtOwnerPages']",
	# 13 | Number of recipients
	"/form[@name='File Information']/text[@automationid='txtOwnerRecipientsCount']",
	# 14 | View
	"/form[@name='File Information']/text[@automationid='txtOwnerViewsCount']",
	# 15 | Viewers
	"/form[@name='File Information']/text[@automationid='txtOwnerViewersCount']",
	# 16 | Total View time
	"/form[@name='File Information']/text[@automationid='txtOwnerTotalViewTime']",
	# 17 | Average view time
	"/form[@name='File Information']/text[@automationid='txtOwnerEverageViewTime']",
	# 18 | Last share time
	"/form[@name='File Information']/text[@automationid='txtOwnerLastSharedTime']",
	# 19 | Last view time
	"/form[@name='File Information']/text[@automationid='txtOwnerLastViewedTime']",
	# 20 | Last activity time
	"/form[@name='File Information']/text[@automationid='txtOwnerLastActivityTime']",
	# 21 | pencil button
	"/form[@name='File Information']/table[@automationid='dgRecipient']//button[@classname='Button']",
	# 22 | Delete current recipient button
	"/form[@name='File Information']/table[@automationid='dgRecipient']/?/?/cell[@classname='DataGridCell' and @text~'^Item:\ FSModel\.Model\.Recip' and @columnindex='3']/button[@classname='Button']",

]


gmwin_recentSentFileChildMenu=[
	# 0 | child menu item
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']/?/?/menuitem[@name='<<filename>>']"
]


gmwin_recentSentFileSubMenu=[
	# 0 | Add new Recipients
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuShare']",
	# 1 | Change Recipient Rights
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuChangeRight']",
	# 2 | View Recipients
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuViewRecipient']",
	# 3 | Track File Views
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuTrackFileView']",
	# 4 | Push File Update
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuPushUpdate']",
	# 5 | Revoke All Access
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuRevoke']",
	# 6 | File Information
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuFileInfo']",
	# 7 | Show In Explorer
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuShowInExplorer']",
	# 8 | Show on FileString.com
	"/form[@name='TrayIconMenuWindow']/form[@classname='Popup']//menuitem[@automationid='mnuViewOnWebsite']",
]


gmwin_fileStringViewer=[
	# 0 | Form
	"/form[@name~'FileString - ']",
	# 1 | Minimize Button
	"/form[@name~'FileString - ']/?/?/button[@automationid='Minimize']",
	# 2 | Maximize button
	"/form[@name~'FileString - ']/?/?/button[@automationid='Maximize']",
	# 3 | Close button
	"/form[@name~'FileString - ']/?/?/button[@automationid='Close']",
	# 4 | Menu File
	"/form[@name~'FileString - ']/?/?/menuitem[@name='File']",
	# 5 | Menu File -> Open
	"/form[@classname='Popup']/?/?/menuitem[@name='Open']",
	# 6 | Menu File -> Open Recent
	"/container[4]/?/?/menuitem[@automationid='ListRecentFile']",
	# 7 | Menu File -> Open Recent -> File
	"/container[3]/container/menuitem", # + index ex:  /container[3]/container/menuitem[1]
	# 8 | Menu FIle -> Print
	"/container[@classname='Popup']/?/?/menuitem[@automationid='mnPrint']",
	# 9 | Menu File -> Close windows
	"/container[@classname='Popup']/?/?/menuitem[@name='Close Window']",
	# 10 | Menu File -> Exit
	"/container[@classname='Popup']/?/?/menuitem[@name='Exit']",
	# 11 | Menu View
	"/form[@name~'FileString - ']/?/?/menuitem[@name='View']",
	# 12 | Menu View -> Zoom In
	"/container[@classname='Popup']/?/?/menuitem[@name='Zoom In']",
	# 13 | Menu View -> Zoom Out
	"/container[@classname='Popup']/?/?/menuitem[@name='Zoom Out']",
	# 14 | Menu View -> Zoom to 
	"/container[@classname='Popup']/?/?/menuitem[@name='Zoom to Fit Window']",
	# 15 | Pop up message when opening expired file
	"/form[@automationid='Window']/text[@automationid='txtMessage']",
	# 16 | Zoom Ratio
	"/form[@name~'^FileString\ -\ ']/combobox[@automationid='cbZoomRatio']"
	# 17 | 
	# 18 | 
	# 19 | 
	# 20 | 
	# 21 | 
	# 22 | 
	# 23 | 


]

gmwin_warningMessageWhenRenameAFile=[
	# 0 | windows
	"/form[@automationid='Window']",
	# 1 | Message: "This file can not be renamed because the name is controlled by the file owner."
	"/form[@automationid='Window']/text[@automationid='tblCaption']",
	# 2 | Do not display this warning again checkbox
	"/form[@automationid='Window']/checkbox[@automationid='chkNotDisplayMsg']",
	# 3 | OK button
	"/form[@automationid='Window']/button[@automationid='btnConform']",
	# 4 | OK button2
	"/form[@automationid='Window']/button[@automationid='btnOK']",
]



gmwin_fileStringTour=[
	# 0 | Form FileString tour
	"/form[@name='FileString Tour']",
	# 1 | Logo FileString
	"/dom[@domain='app.filestring.com']//div[#'header']/img[@src='http://app.filestring.com/Images/Logo/FileStringLogo_White.png']",
	# 2 | WELCOME TO FILESTRING text
	"/dom[@domain='app.filestring.com']//div[#'titlepage']",
	# 3 | WELCOME TO FILESTRING link
	"/dom[@domain='app.filestring.com']//a[#'WelcomeToFileString']",
	# 4 | FIND YOUR WAY AROUND link
	"/dom[@domain='app.filestring.com']//a[#'FindingYourWayAround']",
	# 5 | "STRING" A FILE link
	"/dom[@domain='app.filestring.com']//a[#'StringAFile']",
	# 6 | OPEN RECEIVED FILES link
	"/dom[@domain='app.filestring.com']//a[#'OpeningReceivedFiles']",
	# 7 | RE-SHARE RECEIVED FILES link
	"/dom[@domain='app.filestring.com']//a[#'ReShareAReceivedFile']",
	# 8 | CHANGE FILE RIGHTS link
	"/dom[@domain='app.filestring.com']//a[#'ChangeFileRights']",
	# 9 | TRACK RECIEPIENT FILE VIEWS link
	"/dom[@domain='app.filestring.com']//a[#'TrackRecipientFileViews']",
	# 10 | KEEP FILES UP-TO-DATE link
	"/dom[@domain='app.filestring.com']//a[#'KeepFilesUpToDate']",
	# 11 | REVOKE ACCESS TO FILES link
	"/dom[@domain='app.filestring.com']//a[#'RevokeFileAccess']",
	# 12 | FIND MORE ANSWERS... link
	"/dom[@domain='app.filestring.com']//a[#'FindMoreAnswers']",
	# 13 | content
	"/dom[@domain='app.filestring.com']//div[#'mCSB_1']",
	# 14 | check box
	"/form[@name='FileString Tour']/checkbox[@automationid='chkShowTourNext']",
	# 15 | text Display this tour the next time I close the FileString Viewer
	"/form[@name='FileString Tour']/?/?/text[@name~'^Display\ this\ tour\ the\ nex']",
	# 16 | Close button
	"/form[@name='FileString Tour']/?/?/button[@automationid='Close']",
]



















































































## Below elements is not Application element, they are windows's elements





















gmwin_openingFileString=[
	# 0 | Form
	"/form[@name~'FileString - ']",
	# 1 | Minimize Button
	"/form[@name~'FileString - ']/?/?/button[@automationid='Minimize']",
	# 2 | Maximize button
	"/form[@name~'FileString - ']/?/?/button[@automationid='Maximize']",
	# 3 | Close button
	"/form[@name~'FileString - ']/?/?/button[@automationid='Close']",
	# 4 | Menu File
	"/form[@name~'FileString - ']/?/?/menuitem[@name='File']",
	# 5 | Menu File -> Open
	"/form[@classname='Popup']/?/?/menuitem[@name='Open']",
	# 6 | Menu File -> Open Recent
	"/container[4]/?/?/menuitem[@automationid='ListRecentFile']",
	# 7 | Menu File -> Open Recent -> File
	"/container[3]/container/menuitem", # + index ex:  /container[3]/container/menuitem[1]
	# 8 | Menu FIle -> Print
	"/container[@classname='Popup']/?/?/menuitem[@automationid='mnPrint']",
	# 9 | Menu File -> Close windows
	"/container[@classname='Popup']/?/?/menuitem[@name='Close Window']",
	# 10 | Menu File -> Exit
	"/container[@classname='Popup']/?/?/menuitem[@name='Exit']",
	# 11 | Menu View
	"/form[@name~'FileString - ']/?/?/menuitem[@name='View']",
	# 12 | Menu View -> Zoom In
	"/container[@classname='Popup']/?/?/menuitem[@name='Zoom In']",
	# 13 | Menu View -> Zoom Out
	"/container[@classname='Popup']/?/?/menuitem[@name='Zoom Out']",
	# 14 | Menu View -> Zoom to 
	"/container[@classname='Popup']/?/?/menuitem[@name='Zoom to Fit Window']",
	# 15 | Pop up message when opening expired file
	"/form[@automationid='Window']/text[@automationid='txtMessage']",
	# 16 | 
	# 17 | 
	# 18 | 
	# 19 | 
	# 20 | 
	# 21 | 
	# 22 | 
	# 23 | 


]

gmwin_errorMessageWhenOpenExpiredFile=[
	# 0 | form
	"/form[@automationid='Window']",
	# 1 | test message
	"/form[@automationid='Window']/text[@automationid='txtMessage']",
	# 2 | OK button
	"/form[@automationid='Window']/button[@automationid='btnOK']",
]

fswin_oneTimeUseVariable=[
	# 0 | delete item
	"/form[@title='FileString']/element[@class='ShellTabWindowClass']//container[@caption='ShellView']/?/?/listitem[<<index>>]/picture[@classname='UIImage']",
	# 1 | The folder can not be use ... when change location
	"/container[@title='The folder can''t be used']/?/?/element[@instance='0']/button[@text='OK']",
	# 2 | This computer menu item
	"/container[@title='Browse For Folder']/?/?/tree[@controlid='100']/?/?/treeitem[@text='This PC']",
	# 3 | D driver
	"/container[@title='Browse For Folder']/?/?/tree[@controlid='100']/?/?/treeitem[@text='This PC']/treeitem[@text~'D:']",
	# 4 | Make new Folder
	"/container[@title='Browse For Folder']/button[@text='&Make New Folder']",
	# 5 | OK button of select folder
	"/container[@title='Browse For Folder']/button[@text='OK']",
	# 6 | OK button at move file
	"/form[@name='FileString']/?/?/text[@name='Ok']",
	# 7 | OK button at Device settings
	"/form[@name='Device Settings']/?/?/text[@name='OK']",
	# 8 | Source file supported
	"/form[@title='FileTypeSupported']",
	# 9 | Menu View
	"/form[@title='FileTypeSupported']/element[3]//tabpagelist[@accessiblename='Ribbon tabs']/container[@accessiblename='']/tabpage[@accessiblename='View']",
	# 10 | Detail View 64 bit
	"/form[@processname='explorer' and @class='Net UI Tool Window']//container[@accessiblename='View']/toolbar[@accessiblename='Layout']/container[@accessiblename='Views']/list[@accessiblename='Views']/?/?/listitem[@accessiblename='Details']",
	# 11 | Maximize-Restore button
	"/form[@title='FileTypeSupported']/?/?/button[@automationid='Maximize-Restore']",
	# 12 | close button
	"/form[@title='FileTypeSupported']/?/?/button[@automationid='Close']",
	# 13 | Start downloading file
	"/form[@name='TrayIconMenuWindow']/text[@name~'^Synced\ ']",



]








gmwin_chromeElement=[
	# 0 | stop loading page button
	"/form[@title~'^tempinbox\.com']//toolbar[@accessiblename='Google Chrome Toolbar']/button[@accessiblename='Reload']/picture[@accessiblerole='Graphic']",
	# 1 | 
]




gmwin_installationForm=[
	# 0 | Form
	"/form[@title='Setup - FileString']",
	# 1 | Ready to install text
	"/form[@title='Setup - FileString']/element[@class='TNewNotebook']/?/?/container[@class='TPanel']/?/?/text[@accessiblename='Ready to Install']",
	# 2 | Setup is now ready to begin installing FileString on your computer. text
	"/form[@title='Setup - FileString']/element[@class='TNewNotebook']/?/?/container[@class='TPanel']/?/?/text[@accessiblename~'^Setup\ is\ now\ ready\ to\ beg']",
	# 3 | Message below
	"/form[@title='Setup - FileString']/element[@class='TNewNotebook']/?/?/element[@class='TNewNotebook']/element[@instance='0']/?/?/text[@accessiblename~'^\ CONTROL\ YOUR\ FILES\ EVEN\ ']",
	# 4 | install button
	"/form[@title='Setup - FileString']/?/?/button[@accessiblename='Install']",
	# 5 | Cancel button
	"/form[@title='Setup - FileString']/?/?/button[@accessiblename='Cancel']",
	# 6 | Minimize button
	"/form[@title='Setup - FileString']/?/?/button[@accessiblename='Minimize']",
	# 7 | Close button
	"/form[@title='Setup - FileString']/?/?/button[@accessiblename='Close']"
]



gmwin_contextMenuOfFCSFile=[
	# 0 | File Information
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='File Information']",
	# 1 | Show on FileString.com
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Show on FileString.com']",
	# 2 | Re-Share this File
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Re-Share this File']",
	# 3 | Change Recipient Rights
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Change Recipient Rights']",
	# 4 | View Recipients
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='View Recipients']",
	# 5 | Track File Views
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Track File Views']",
	# 6 | Revoke Recipient Access
	"/contextmenu[@class='#32768' and @instance='1']/?/?/menuitem[@accessiblename='Revoke Recipient Access']"


]

# gmwin_contextMenuOfFSCFile=[
# 	# 0 | Testing account 6 folder
# 	"/form[@title='Test Testingaccount6']",
# 	# 1 | Maximize button
# 	"/form[@title='Test Testingaccount6']/?/?/button[@automationid='Maximize-Restore']",
# 	# 2 | Close button
# 	"/form[@title='Test Testingaccount6']/?/?/button[@automationid='Close']",
# 	# 3 | item in list
# 	"/form[@title='Test Testingaccount6']/element[@class='ShellTabWindowClass']//container[@caption='ShellView']/?/?/listitem[@automationid='<<index>>']/text[@automationid='System.ItemNameDisplay']",
# 	# 4 | Menu View
# 	"/form[@title='Test Testingaccount6']/element[3]//tabpagelist[@accessiblename='Ribbon tabs']/container[@accessiblename='']/tabpage[@accessiblename='View']",
# 	# 5 | Details button
# 	"/form[@processname='explorer' and @class='Net UI Tool Window']//container[@accessiblename='View']/toolbar[@accessiblename='Layout']/container[@accessiblename='Views']/list[@accessiblename='Views']/?/?/listitem[@accessiblename='Details']",
# 	# 6 | 
# ]

base_locator="/form[@name='Your Preferences']"

gmwin_yourPreferences=[
	# 0 | Your Preferences form
	base_locator,
	# 1 | Your Time Zone title
	base_locator+"/text[@name='Your Time Zone']",
	# 2 | Time zone combobox
	"/form[@name='Your Preferences']/combobox[@automationid='CbbTimeZone']",
	# 3 | Sharing Defaults text
	"/form[@name='Your Preferences']/text[@name='Sharing Defaults']",
	# 4 | By default, when I share files: text
	"/form[@name='Your Preferences']/text[@name~'^By\ default,\ when\ I\ share\ ']",
	# 5 | Set access rights to: text
	"/form[@name='Your Preferences']/text[@name='Set access rights to: ']",
	# 6 | Set access rights to combobox
	"/form[@name='Your Preferences']/combobox[@automationid='cbAccessRights']",
	# 7 | Allow Printing checkbox
	"/form[@name='Your Preferences']/checkbox[@automationid='chkAllowPrinting']",
	# 8 | Add a watermark checkbox
	"/form[@name='Your Preferences']/checkbox[@automationid='chkAddWatermark']",
	# 9 | Other Notifications title
	"/form[@name='Your Preferences']/text[@name='Other Notifications']",
	# 10 | Notify me when... text
	"/form[@name='Your Preferences']/text[@name='Notify me when...']",
	# 11 | My files are re-shared checkbox
	"/form[@name='Your Preferences']/checkbox[@automationid='chkNotifyReshared']",
	# 12 | Another user revokes a recipient's access to a file I own checkbox
	"/form[@name='Your Preferences']/checkbox[@automationid='chkNotifyRevoke']",
	# 13 | A recipient's access to files I own expires checkbox
	"/form[@name='Your Preferences']/checkbox[@automationid='chkNotifyExpires']",
	# 14 | View Notifications title
	"/form[@name='Your Preferences']/text[@name='Viewing Notifications']",
	# 15 | Notify me when my files are viewed by... text
	"/form[@name='Your Preferences']/text[2]",
	# 16 | Direct Recipients: text
	"/form[@name='Your Preferences']/text[3]",
	# 17 | Direct Recipients - Every view radio button
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioViewDirectEvery']",
	# 18 | Direct Recipients - First View radio button
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioViewDirectFirst']",
	# 19 | Direct Recipients - Never radio button
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioViewDirectNever']",
	# 20 | Downstream Recipients: text
	"/form[@name='Your Preferences']/text[4]",
	# 21 | Downstream Recipients - Every View radio button
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioViewDownstreamEvery']",
	# 22 | Downstream Recipients - First view radio button
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioViewDownstreamFirst']",
	# 23 | Downstream Recipients - Never radio button
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioViewDownstreamNever']",
	# 24 | Printing Notifications title
	"/form[@name='Your Preferences']/text[@name='Printing Notifications']",
	# 25 | Notify me when my files are printed by... text
	"/form[@name='Your Preferences']/text[6]",
	# 26 | Direct Recipients: text
	"/form[@name='Your Preferences']/text[7]",
	# 27 | Direct Recipients - Every Time
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioPrintDirectEvery']",
	# 28 | Direct Recipients - First Time
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioPrintDirectFirst']",
	# 29 | Direct Recipients - Never
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioPrintDirectNever']",
	# 30 | Downstream Recipients: text
	"/form[@name='Your Preferences']/text[8]",
	# 31 | Downstream Recipients - Every Time
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioPrintDownstreamEvery']",
	# 32 | Downstream Recipients - First Time
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioPrintDownstreamFirst']",
	# 33 | Downstream Recipients - Never
	"/form[@name='Your Preferences']/radiobutton[@automationid='radioPrintDownstreamNever']",
	# 34 | OK button
	"/form[@name='Your Preferences']/button[@automationid='btnOK']",
	# 35 | Cancel button
	"/form[@name='Your Preferences']/button[@automationid='btnCancel']",

]


gmwin_helpCenterChromeForm=[
	# 0 | Help center title
	"/form[@title~'^FileString\ Customer\ Feedb']/container[@accessiblename='Google Chrome']/?/?/container[@accessiblehelp='TopContainerView']/?/?/tabpage[@accessiblename~'^FileString\ Customer\ Feedb']",
	# 1 | Close button
	"/form[@title~'^FileString\ Customer\ Feedb']/container[@accessiblename='Google Chrome']//tabpage[@accessiblename~'^FileString\ Customer\ Feedb']/button[@accessiblename='Close']",
]











