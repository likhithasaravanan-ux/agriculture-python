import pandas as pd

crop = {'wheat': {
        'fertilizer':'Urea with nitrigon source and DAP',
        'pesticides':'Imidacloprid controls aphids and chiorpyrifos for control soil insects',
        'climate':'rain fall low and moderate'},
    'rice': {
        'fertilizer':'Urea for fromote leaf grouth ',
        'pesticides':'Buprofezin',
        'climate':'high'},
    'cotton': {
        'fertilizer':'Nitrogen and Phosphorus',
        'pesticides':'thiamethoxam controle white fly',
        'climate':'rain fall in moderate,warm and sunny in climate'},
    'maize':{
        'fertilizer':'DAP for 20-25 days',
        'pesticides':'spinosad controls leaf pests',
        'climate':'rain fall in moderate and warm climate'},
    'sugarcane':{
        'fertilizer':'(MOP) muriate of potash',
        'pesticides':'fipronil controles soil pests',
        'climate':'hot and numid in climate and moderate rain fall'},
    'groundnut':{
        'fertilizer':'DAP and Gypsum',
        'pesticides':'Chlorpyrifos control leaf eating caterpillars',
        'climate':'rain fall in low and moderate , climate is in warm and dry'},
    'paddy':{
        'fertilizer':'Urea and DAP',
        'pesticides':'Buprofezin control plant hopper',
        'climate':'standing water needed, climate in humid'},
    'sunflower':{
        'fertilizer':'Nitrogen(rich) and single super phospate',
        'pesticides':'Quinalphos'},
        'climate':'low rain fall and sunny and dry climate'
       }

print('1.Black soil')
print('2.Red soil')
print('3.Alluvial soil')
print('4.Clay soil')
print('------select the type of soil in your land------')
f_soil=int(input('--enter an soil option--'))
if (f_soil==1):
    print('you have black soil in your land')
    print('----------------------------------')
    print('Best crops for Black soil are:')
    print('1.cotton')
    print('2.sugarcane')
    f_crop=int(input('enter option for given crop'))
    if(f_crop==1):
        print('\nyou are selected cotton for croping in black soil')
        a=crop["cotton"]["fertilizer"]
        b=crop['cotton']['pesticides']
        c=crop['cotton']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    elif (f_crop==2):
        print('\nyou are selected oil seeds for croping in black soil')
        a=crop['sugarcane']['fertilizer']
        b=crop['sugarcane']['pesticides']
        c=crop['sugarcane']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    else:
        print('invalid input')
elif (f_soil==2):
    print('you have red soil in your land')
    print('----------------------------------')
    print('Best crops for red soil are:')
    print('1.wheat')
    print('2.rice')
    f_crop=int(input('enter option for given crop'))
    if(f_crop==1):
        print('\nyou are selected wheat for croping in red soil')
        a=crop['wheat']['fertilizer']
        b=crop['wheat']['pesticides']
        c=crop['wheat']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    elif (f_crop==2):
        print('you are selected rice for croping in red soil')
        a=crop['rice']['fertilizer']
        b=crop['rice']['pesticides']
        c=crop['rice']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    else:
        print('invalid input')
elif (f_soil==3):
    print('\nyou have red soil in your land')
    print('----------------------------------')
    print('Best crops for red soil are:')
    print('1.maize')
    print('2.ground nut')
    f_crop=int(input('enter option for given crop'))
    if(f_crop==1):
        print('\nyou are selected wheat for croping in red soil')
        a=crop['maize']['fertilizer']
        b=crop['maize']['pesticides']
        c=crop['maize']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    elif (f_crop==2):
        print('\nyou are selected rice for croping in red soil')
        a=crop['groundnut']['fertilizer']
        b=crop['groundnut']['pesticides']
        c=crop['groundnut']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    else:
        print('invalid input')
elif (f_soil==4):
    print('you have red soil in your land')
    print('----------------------------------')
    print('Best crops for red soil are:')
    print('1.sunflower')
    print('2.paddy')
    f_crop=int(input('enter option for given crop'))
    if(f_crop==1):
        print('\nyou are selected wheat for croping in red soil')
        a=crop['sunflower']['fertilizer']
        b=crop['sunflower']['pesticides']
        c=crop['sunflower']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    elif (f_crop==2):
        print('\nyou are selected rice for croping in red soil')
        a=crop['paddy']['fertilizer']
        b=crop['paddy']['pesticides']
        c=crop['paddy']['climate']
        print("fertilizer are : ",a)
        print("pesticides are : ",b)
        print("climate for that crop : ",c)
    else:
        print('invalid input')
else:
    print('invalid input')
# Simple static weather report
print("\n. Weather Forecast (Next 7 Days):")
print("Day 1-2: Sunny ")
print("Day 3-4: Partly Cloudy ")
print("Day 5: Light Rain ")
print("Day 6-7: Sunny ")

print("\n. Farming Advice:")
print("• Water crops in early morning")
print("• Avoid spraying pesticides during rain")
print("• Use organic manure once a month")
