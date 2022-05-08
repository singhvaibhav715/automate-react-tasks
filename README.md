# THIS PYTHON SCRPIT CAN SAVE YOUR LOT OF TIME IF YOU ARE A REACTJS DEVELOPER
## FOLLOW THE FOLLOWING STEPS TO USE THIS SCRIPT IN EFFICIENT WAY

### 1. Download this "automate.py" file and paste into your root folder i.e along with scr or public folder
### 2. Command to create components with boilerplate code
###    2.1 python ./automate.py default-path include-css component1 component2 
           ( This will create the components with css file inside "src/components" and structure will be --)
              component1
                Component1.js
                Component1.css
              component2
                Component2.js
                Component2.css
                
###    2.2 python ./automate.py default-path no-css component1 component2
            ( This will create the components without css file inside "src/components" and structure will be --)
            component1
                Component1.js
              component2
                Component2.js
###   2.3 python ./automate.py custom-path src>other-folder include-css otherComponent1 otherComponent2
          ( This will create the components with css file inside "src/other-folder" and structure will be --)
              other-folder
                otherComponent1
                  OtherComponent1.js
                  OtherComponent1.css
                otherComponent2
                  OtherComponent2.js
                  OtherComponent2.css
