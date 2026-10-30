def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit.capitalize()}: {qiymat}")

talaba_info(ism="Ali", kurs=2, shahar="Samarqand")