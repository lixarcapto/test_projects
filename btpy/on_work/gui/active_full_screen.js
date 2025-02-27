


export function active_full_screen() {
    const elemento = document.documentElement;
    if (elemento.requestFullscreen) {
      elemento.requestFullscreen();
    } else if (elemento.mozRequestFullScreen) { /* Firefox */
      elemento.mozRequestFullScreen();
    } else if (elemento.webkitRequestFullscreen) { /* Chrome, Safari */
      elemento.webkitRequestFullscreen();
    } else if (elemento.msRequestFullscreen) { /* IE/Edge */
      elemento.msRequestFullscreen();
    }
  }