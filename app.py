import qrcode
import os

link_sites ={
    "Tik_tok": "https://www.tiktok.com/foryou",
    "gmail":"https://mail.google.com/mail/u/0/#inbox",
    "Youtube":"https://www.youtube.com/"
}
 # criando um diretorio
if not os.path.exists('qr_codes'):
    os.makedirs('qr_codes')
sites = link_sites

#repeticao para gerar todos qr codes
for meus_sites in sites:
    print(sites[meus_sites])

    imagem_qrcode = qrcode.make(sites[meus_sites])
    imagem_qrcode.save(f"qr_codes/qrcode_{meus_sites}.png")
