# LiffLogin
for LINE LIFF Login and paste LINE profile to google form when user (police) register ฟอร์มทะเบียนใช้งานระบบติดตามสถานะรายงานชันสูตร
Requirements : 
	1. สร้าง prefilled google form
	2. Webhooks : ต้องมี https แต่ใช้ google app script ไม่ได้ เพราะ deploy ทุกครั้ง url จะเปลี่ยน ซึ่งต้องใช้การ deploy 2 ครั้ง ถึงใช้ได้ (ครั้งแรก copy url ไปใส่ใน LIFF ก่อน แล้วได้ liff id มาใส่ใน code index.html แล้วจึง deploy อีกรอบ จึงใช้ได้)
	3. LIFF id ดังกล่าวแล้ว (สร้าง LINE login 1 channel)
  4. LIFF url เอาไปใส่ใน Richmenu
