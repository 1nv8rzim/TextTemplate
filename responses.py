"""
stores responses to be used for TextTemplate.py
"""
responses = {
    'close':(0,'I would like to thank you for contacting Cisco TAC Center. As we have agreed, I will now close this case. \n\nIt has been a pleasure working in this service request (SR) number: '\
        '<CASE NUMBER>\n\nPlease remember, if you need any further assistance, do not hesitate to contact Cisco TAC Center, below is my contact information and working schedule if you need it in '\
            'the future. Also you can visit https://help.webex.com/ for frequently asked questions.\n\nThank you for choosing Cisco; it is always a pleasure to help you.'),
    'open':(0,'Hi <CUSTOMER NAME>,\n\nMy name is Max and I am a member of the Cisco Webex TAC Team. I have accepted case SR <CASE NUMBER> and will be helping you resolve your issue. Looking at your '\
        'case, <CASE DESCRIPTION>\n\nTo investigate further, I will need the following from you:\n\t*\n\nPlease feel free to reach out with any updates. I also kindly ask you reply all to all following '\
            'correspondence so that your emails will be populated to our case tracking. Upon the providing the above information, I will be able to look further into your case.')
} 