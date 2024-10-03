import qrcode

link_sites ={
    "Tik_tok": "https://www.tiktok.com/foryou",
    "gmail":"https://mail.google.com/mail/u/0/#inbox",
    "Youtube":"https://www.youtube.com/"
}

sites = link_sites

for meus_sites in sites:
    print(sites[meus_sites])

    imagem_qrcode = qrcode.make(sites[meus_sites])
    imagem_qrcode.save(f"qrcode_{meus_sites}.png")