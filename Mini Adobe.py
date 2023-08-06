# MINI ADOBE : 
import os
import rawpy
import imageio
from PIL import Image
import cv2
import glob
import math

def design(s,end="\n"):
    print("--------------------------------------------------") 
    print(s,end=end)
    print("--------------------------------------------------") 

# 1 : 
# THE FUNCTION TO CONVERT AN IMAGE : 
def convertImage():
    try:
        # SAVE THE PATH OF THE DIRECTORY WHERE WE WILL WORK : 
        design(r'[SUGGESTION] THE PATH OF OUR IMAGE FILE DIRECTORY : C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Image_Handeling')
        o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
        if o.upper()=="YES":
            directory = input("[ENTER] THE PATH OF THE IMAGE FILE DIRECTORY : ")
        else:
            directory=r"C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Image_Handeling"

        # GO TO THE DIRECTORY WHERE WE WILL WORK : 
        os.chdir(directory)
        design("WE ARE NOW : "+directory)

        # LIST OF FILES AND DIRECTORIES : 
        print("LIST OF FILES AND FOLDERS : ")
        design(os.listdir(directory))
        
        # CHOOSE OUR IMAGE FILE : 
        name=input("[ENTER] OUR IMAGE FILE IS : ")

        # Using cv2.imread() method : to read the image in openCV
        imgCV = cv2.imread(name)
        # Using Image.open() method : to read the image in PILLOW
        imgPIL = Image.open(name)

        # RENAME THE FILE AT EACH STEP OF THE PATH : 
        rename=name
        # FOLLOW THE CONVERTION PATH : 
        followedPath=[]

        # CREATE AND GO TO THE PATH OF THE DIRECTORY WHERE WE WANT TO SAVE THE CONVERTED IMAGE : 
        design(r'[SUGGESTION] THE PATH OF OUR SAVED IMAGE FILE DIRECTORY : C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Image_Handeling\Saved_Converted_Image')
        o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
        if o.upper()=="YES":
            directory=input("[ENTER] THE PATH OF THE SAVED IMAGE FILE DIRECTORY : ")
        else:
            directory=r"C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Image_Handeling\Saved_Converted_Image"
        
        directory+='/'+name[:name.index(".")]
        
        if not os.path.exists(directory):
            os.mkdir(directory)
        
        os.chdir(directory)
        design("WE ARE NOW :"+directory)

        # ROTATE IMAGE : 
        print("----------------------------------------------------") 
        o=input('[OPTION] DO YOU WANT TO ROTATE THE IMAGE : YES/NO : ')
        print("----------------------------------------------------")
        if o.upper()=="YES":
            rename=name[:name.index(".")]+"_rotated"+name[name.index("."):]
            followedPath.append(f"ROTATION [{rename}]")

            # THE ANGLE OF THE IMAGE ROTATION : 
            design('[SUGGESTION] ENTER ONLY DEGREE VALUE (i.e., 0<=angle<=360)')
            angle=input("[ENTER] THE ANGLE YOU WANT TO ROTATE : ")

            # ROTATE IMAGE : 
            imgPIL = imgPIL.rotate(int(angle))

            # SAVE IMAGE :
            imgPIL.save(rename)
        else:
            # SAVE IMAGE :
            imgPIL.save(rename)
        
        # COMPRESS IMAGE :
        print("------------------------------------------------------") 
        o=input('[OPTION] DO YOU WANT TO COMPRESS THE IMAGE : YES/NO : ')
        print("------------------------------------------------------")
        if o.upper()=="YES":
            imgPIL = Image.open(rename)
            rename=rename[:rename.index(".")]+"_compressed"+rename[rename.index("."):]
            followedPath.append(f"COMPRESSION [{rename}]")

            # THE COMPRESSION RATE OF THE IMAGE : 
            design('[SUGGESTION] ENTER ONLY PERCENTAGE VALUE (i.e., 0<=rate<=100)')
            rate=int(input("[ENTER] THE RATE YOU WANT TO COMPRESS : "))

            # COMPRESS IMAGE : 
            # DIMENSION : width x height
            width, height = imgPIL.size
            if width > 1000 or height > 1000:
                width = width*(1-rate/100)
                height = height*(1-rate/100)
            imgPIL = imgPIL.resize((int(math.floor(width)), int(math.floor(height))), Image.ANTIALIAS)

            # SAVE IMAGE :
            imgPIL.save(rename,optimize=True,quality=(100-rate))

        # CONVERT IMAGE : 
        ext=name[name.index(".")+1:]
        print("-----------------------------------------------------") 
        o=input('[OPTION] DO YOU WANT TO CONVERT THE IMAGE : YES/NO : ')
        print("-----------------------------------------------------")
        if o.upper()=="YES":
            imgCV=cv2.imread(rename)
            
            # THE CONVERTED EXTENSION OF THE IMAGE : 
            print("-----------------------------------------------------------")
            print("[SUGGESTION] HERE IS YOUR EXTENSION TO CONVERT THE IMAGE : ")
            l="AAI, ART, ARW, AVS, BPG, BMP, BMP2, BMP3, BRF, CALS, CGM, CIN, CMYK, CMYKA, CR2, CRW, CUR, CUT, DCM, DCR, DCX, DDS, DIB, DJVU, DNG, DOT, DPX, EMF, EPDF, EPI, EPS, EPS2, EPS3, EPSF, EPSI, EPT, EXR, FAX, FIG, FITS, FPX, GIF, GPLT, GRAY, HDR, HEIC, HPGL, HRZ, ICO, ISOBRL, ISBRL6, JBIG, JNG, JP2, JPT, J2C, J2K, JPEG/JPG, JXR, MAT, MONO, MNG, M2V, MRW, MTV, NEF, ORF, OTB, P7, PALM, PAM, PBM, PCD, PCDS, PCL, PCX, PDF, PEF, PES, PFA, PFB, PFM, PGM, PICON, PICT, PIX, PNG, PNG8, PNG00, PNG24, PNG32, PNG48, PNG64, PNM, PPM, PSB, PSD, PTIF, PWB, RAD, RAF, RGB, RGBA, RGF, RLA, RLE, SCT, SFW, SGI, SID, SUN, SVG, TGA, TIFF, TIM, UIL, VIFF, VICAR, VBMP, WDP, WEBP, WPG, X, XBM, XCF, XPM, XWD, X3F, YCbCr, YCbCrA, YUV".split(", ")
        
            j=1
            for i in l:
               print(str(j)+" : "+i)
               j+=1
            print("-----------------------------------------------------------") 
            e=int(input("[ENTER] THE EXTENSION INDEX NUMBER : "))
            ext=l[e-1].lower()

            rename=rename[:rename.index(".")]+"_converted."+ext
            followedPath.append(f"CONVERSION [{rename}]")

            # CONVERT AND SAVE IMAGE : 
            cv2.imwrite(rename, imgCV) 
        
        design("[CONCLUSION] AFTER CONVERTING IMAGE : ")
                
        # FOLLOWED PATH :
        print("--------------------------------------------------")
        print("FOLLOWED PATH : ",end="")
        for i in followedPath:
            print(i+" ->",end=" ")
        print(f"FINAL [{name[:name.index('.')]+'_final.'+ext}]")
        print("--------------------------------------------------")

        # SAVE FINAL IMAGE : 
        imgCV=cv2.imread(rename)
        cv2.imwrite(name[:name.index('.')]+'_final.'+ext,imgCV)

        # LIST OF FILES AND DIRECTORIES : 
        print("LIST OF FILES AND FOLDERS :")
        design(os.listdir(directory))
    except IOError:
        # ERROR : 
        design("[ERROR] THERE ARE ERRORS IN THE CODE")
        pass

# 2 :
# THE FUNCTION TO CONVERT RAW IMAGES TO JPG IMAGES : 
def convertRawImages():
    try:
        # SAVE THE PATH OF THE DIRECTORY WHERE WE WILL WORK : 
        design(r'[SUGGESTION] THE PATH OF OUR RAW IMAGEs FILE DIRECTORY : C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Raw_Files')
        o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
        if o.upper()=="YES":
            sourceDirectory = input("[ENTER] THE PATH OF THE RAW IMAGEs FILE DIRECTORY : ")
        else:
            sourceDirectory = r"C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Raw_Files"

        # LIST OF FILES AND DIRECTORIES : 
        print("LIST OF FILES AND FOLDERS :")
        design(os.listdir(sourceDirectory))

        design(r'[SUGGESTION] THE PATH OF OUR CONVERTED RAW IMAGE FILEs DIRECTORY : C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Converted_Raw_Files')
        o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
        if o.upper()=="YES":
            destinationDirectory = input("[ENTER] THE PATH OF THE CONVERTED RAW IMAGE FILEs DIRECTORY : ")
        else:
            destinationDirectory = r"C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Converted_Raw_Files"

        design('[SUGGESTION] ENTER ONLY THE EXTENSION NAME (i.e., not .)')
        # REAL FILE EXTENSION
        rfext=input("[ENTER] RAW FILE EXTENSION : ")
        # CONVERTED FILE EXTENSION
        cvext=input("[ENTER] CONVERTED FILE EXTENSION : ")

        # GO TO THE DESTINATION DIRECTORY : 
        os.chdir(destinationDirectory)
        design("WE ARE NOW : "+destinationDirectory)

        design('[CONVERTING] STARTED')
        n=1
        for img in sorted(glob.glob(sourceDirectory+'\*.'+rfext),key=os.path.getmtime):
            #GET ALL THE PIXELS FROM THE SELECTED IMAGE : 
            try:
                with rawpy.imread(img) as raw:
                    rgb = raw.postprocess()
            except:
                design("THE FILE "+img+" IS NOT PRESENT HERE.")
                continue

            #SET THE CONVERTED IMAGE NAME : 
            convertedImageName = img[img.rindex('\\')+1:img.index('.')+1]+cvext

            os.chdir(destinationDirectory)

            #SAVE THE CONVERTED IMAGE : 
            imageio.imsave(convertedImageName, rgb)

            print(str(n)+" : "+convertedImageName)
            n+=1
        design('[CONVERTING] ENDED')
    
        design("[CONCLUSION] AFTER CONVERTING IMAGEs : ")
    
        design("IN TOTAL "+str(n-1)+" NUMBER OF IMAGES CONVERTED SUCCESSFULLY FROM "+sourceDirectory+" TO "+destinationDirectory)

        # LIST OF FILES AND DIRECTORIES : 
        print("LIST OF FILES AND FOLDERS :")
        design(os.listdir(destinationDirectory))
    
    except:
        # ERROR : 
        design("[ERROR] THERE ARE ERRORS IN THE CODE")
        pass

# 3 :
# THE FUNCTION CREATE AN TIMELAPSE :
def CreateTimelapse(name):
    try:
        design(r'[SUGGESTION] THE PATH OF OUR IMPORTED FILEs DIRECTORY : C:/Users/junil/Desktop\Python\Projects\Project 2 - Mini Adobe\Converted_Raw_Files')
        o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
        if o.upper()=="YES":
            importDirectory = input("[ENTER] THE PATH OF THE IMPORTED FILEs DIRECTORY : ")
        else:
            importDirectory = r"C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Converted_Raw_Files"

        # GO TO THE IMPORT DIRECTORY : 
        os.chdir(importDirectory)
        design("WE ARE NOW : "+importDirectory)

        design(r'[SUGGESTION] THE PATH OF OUR EXPORTED FILEs DIRECTORY : C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Created_Timelapse')
        o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
        if o.upper()=="YES":
            exportDirectory = input("[ENTER] THE PATH OF THE EXPORTED FILEs DIRECTORY : ")
        else:
            exportDirectory = r"C:\Users\junil\Desktop\Python\Projects\Project 2 - Mini Adobe\Created_Timelapse"

        design('[SUGGESTION] ENTER ONLY THE EXTENSION NAME (i.e., not .)')
        ext=input("[ENTER] FILE EXTENSION : ")

        images=sorted(glob.glob(importDirectory+'\*.'+ext),key=os.path.getmtime)

        # GO TO THE EXPORT DIRECTORY : 
        os.chdir(exportDirectory)
        design("WE ARE NOW : "+exportDirectory)

        img = cv2.imread(images[0])
        height, width, layers = img.shape
        size = (width,height)

        name+=".mp4"

        design('[CREATING] STARTED')
        n=len(images)
        writer = cv2.VideoWriter(name,cv2.VideoWriter_fourcc(*'DIVX'), 3, size)
        for file in images:
            n-=1
            frame = cv2.imread(file)
            print(str(n)+" : "+file)
            writer.write(frame)
        writer.release()
        design('[CREATING] ENDED')
    
        design("[CONCLUSION] AFTER CREATING TIMELAPSE : ")
        
        design("TIMELAPSE "+name+" CREATED SUCCESSFULLY")

        # LIST OF FILES AND DIRECTORIES : 
        print("LIST OF FILES AND FOLDERS :")
        design(os.listdir(exportDirectory))
    except:
        # ERROR : 
        design("[ERROR] THERE ARE ERRORS IN THE CODE")
        pass

# MENU : 
while True:
    print("""
    --------------------------
    [OPTION] CHOOSE AN OPTION: 
    1. CONVERT AN IMAGE
    2. CONVERT RAW IMAGES
    3. CREATE TIMELAPSE
    4. BREAK
    --------------------------
    """)
    c=int(input())
    if c==1:
        convertImage()
    elif c==2:
        convertRawImages()
    elif c==3:
        n=input("ENTER THE TIMELAPSE NAME: ")
        CreateTimelapse(n)
    elif c==4:
        break
    else:
        continue