


from btpy.Btpy import Btpy
from tkupg.Tkupg import Tkupg
from geng.Geng import Geng
from geng.Geng import Go

def main():
   window = Tkupg.window()
   window.set_full_screen()
   painter = Tkupg.painter(window)
   painter.pack_in_axe(painter\
            .AXE_EXPANSION.BOTH)
   src = "../res/image/girl_pix_test.png"
   pod = None
   scene = Geng.create_scene_matrix(5, 5)
   class GoPerson(Go):
      def __init__(self, id) -> None:
         super().__init__(id)
         self.src_image = src
         self.is_a_walker = True
         self.set_is_mortal([0, 100])
         self.n = 0
         
      def update(self):
         super().update()
         self.n += 1
         if(self.n >= 10):
            self.launch_transform("GoVegetable")
   
   go = GoPerson("1")
   scene.insert_go(go)
   go2 = GoPerson("2")
   go2.is_the_star = True
   scene.insert_go(go2)
   def action():
      scene.update()
      pod_list = scene.render()
      painter.draw_pod_array(pod_list)
   Btpy.repeat_in_thread(0.8, action, 40)
   window.start()



main()