import package.sound.echo              #모듈을 import로 실행하기
import package.graphic.render
package.sound.echo.echo_test()
package.graphic.render.render_test()

from package.sound import echo         #모듈이 있는 디렉토리까지 from ... import  
echo.echo_test()                       #이용하여 실행하기

from package.sound.echo import echo_test   #모듈 함수를 직접 import하여 사용하기
echo_test()

from package.sound import *   #*은 파일 전체
echo.echo_test()

from package.graphic.render import render_test
render_test()