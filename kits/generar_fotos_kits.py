import sys, json
from PIL import Image, ImageDraw, ImageFont, ImageOps
src, out = sys.argv[1], sys.argv[2]
kits = json.load(open(sys.argv[3]))
BG=(245,242,225); WINE=(112,32,44)
W=H=2048; M=70; G=36; FOOT=230
fb=ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',92)
fs=ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',54)
def tile(path,w,h):
    im=Image.open(f'{src}/{path}').convert('RGB')
    im=ImageOps.fit(im,(w,h),Image.LANCZOS,centering=(0.5,0.5))
    mask=Image.new('L',(w,h),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,w-1,h-1],36,fill=255)
    return im,mask
for k in kits:
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    items=k['items']; n=len(items); area_h=H-M-FOOT
    if n==2:
        w=(W-2*M-G)//2; h=area_h-M
        pos=[(M,M),(M+w+G,M)]; sizes=[(w,h)]*2
    else:
        w=(W-2*M-G)//2; h=(area_h-M-G)//2
        pos=[(M,M),(M+w+G,M),(M,M+h+G),(M+w+G,M+h+G)]; sizes=[(w,h)]*4
    for p,(x,y),(w_,h_) in zip(items,pos,sizes):
        im,mask=tile(p,w_,h_); c.paste(im,(x,y),mask)
    # plus badges
    def plus(cx,cy):
        r=52; d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=WINE)
        d.text((cx,cy-4),'+',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',80),fill=BG,anchor='mm')
    if n==2: plus(W//2, M+(area_h-M)//2)
    else:
        plus(W//2, M+h//2); plus(W//2, M+h+G+h//2); plus(M+w//2, M+h+G//2); plus(M+w+G+w//2, M+h+G//2)
    fy=H-FOOT
    d.text((W//2,fy+70),k['title'],font=fb,fill=WINE,anchor='mm')
    d.text((W//2,fy+160),k['sub'],font=fs,fill=(90,70,60),anchor='mm')
    c.save(f"{out}/{k['file']}",quality=92)
    print('ok',k['file'])
