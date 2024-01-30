def print_list(your_list):
    for item in your_list:
        print(item, end=" ")

def main():
    MeyvelerVeSayılar = ["elma=", 5, "kivi=", 12]

    while True:
        yukselt = input("Listedeki sayıyı yükseltmek için 'z', Çıkmak için 'x' tuşuna basın: ")
        print("Mevcut Sayılar:", end=" ")
        print_list(MeyvelerVeSayılar)

        if yukselt == 'z':
            MeyvelerVeSayılar[1] += 1
            MeyvelerVeSayılar[3] += 1
        elif yukselt == 'x':
            print("\nProgram kapatılıyor...")
            break
        else:
            print("\nGeçersiz giriş! Lütfen 'z' veya 'x' tuşuna basın.")

if __name__ == "__main__":
    main()