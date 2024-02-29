tol = 0.3;
Wall = 3;
M3 = 3/2+tol;
Smoothness = 100;


x_alu = 15;
x_corner = 45;
x_link = 10;
z_link = 1.5+tol;
alu_groove = 3;

z_slider = 30;

l_Extru01 = 150;
l_Extru02 =  50;
l_Extru03 =  300;
l_Extru04 =  200;
LED_Colour = [[1,0,0],[0,1,0],[0,0,1],[1,1,0]];
LED_Colour_Light = [[1,0,0,0.1],[0,1,0,0.1],[0,0,1,0.1],[1,1,0,0.1]];

LED = 5/2;
r_LED = 6.2/2+tol;
R_LED = 7.5/2+tol;
h_LED = 1.5;

Platform = 10;
Base = 10;
Top = 10;
Basler = 10;
Basler_Holder = 10;
IR_Cam_Holder = 1;
Basler_Holder_Full = 1;
LED_Holder = 10;
5mm_LED = 10;
Illumination = 10;
Optogenetics = 10;
 
if (Platform == 1){Platform();}
if (Base == 1){Base();} 
if (Top == 1){Top();} 
if (Basler == 1){translate([0,0,2*x_alu+l_Extru02+2/3*l_Extru03+l_Extru04+z_slider])Basler();} 
if (Basler_Holder == 1){Basler_Holder();} 
if (IR_Cam_Holder == 1){IR_Cam_Holder();} 
if (LED_Holder == 1){LED_Holder();}
if (Optogenetics == 1){translate([0,0,Opto_Height])Optogenetics();}


module Platform(){
    color([0.8,0.8,0.8,0.5])translate([x_alu/2,x_alu/2,l_Extru02+1.5*x_alu])cube([l_Extru01,l_Extru01,Wall]);
}
module Base(){
    translate([0,0,x_alu])rotate([0,90,0]){
        Alu_Extru(l_Extru01);
        translate([0,0,l_Extru01+x_alu])rotate([-90,0,0])Alu_Extru(l_Extru01);
        translate([0,l_Extru01+x_alu,l_Extru01+x_alu])rotate([-180,0,0])Alu_Extru(l_Extru01);
        translate([0,l_Extru01+x_alu,0])rotate([-270,0,0])Alu_Extru(l_Extru01);
    }
    
    translate([x_alu,l_Extru01-x_alu,x_alu])Alu_Extru(l_Extru02);
    translate([l_Extru01-x_alu,l_Extru01-x_alu,x_alu])Alu_Extru(l_Extru02);
    translate([x_alu,x_alu,x_alu])Alu_Extru(l_Extru02);
    translate([l_Extru01-x_alu,x_alu,x_alu])Alu_Extru(l_Extru02);
    
    translate([0,0,x_alu+l_Extru02+x_alu])rotate([0,90,0]){
        Alu_Extru(l_Extru01);
        translate([0,0,l_Extru01+x_alu])rotate([-90,0,0])Alu_Extru(l_Extru01);
        translate([0,l_Extru01+x_alu,l_Extru01+x_alu])rotate([-180,0,0])Alu_Extru(l_Extru01);
        translate([0,l_Extru01+x_alu,0])rotate([-270,0,0])Alu_Extru(l_Extru01);
    }
    
    translate([0,0,2*x_alu+l_Extru02])Alu_Corner();
    translate([l_Extru01+x_alu,0,2*x_alu+l_Extru02])rotate([0,0,90])Alu_Corner();
    translate([l_Extru01+x_alu,l_Extru01+x_alu,2*x_alu+l_Extru02])rotate([0,0,180])Alu_Corner();
    translate([0,l_Extru01+x_alu,2*x_alu+l_Extru02])rotate([0,0,270])Alu_Corner();
    
    translate([x_corner+tol,0,2*x_alu+l_Extru02])Alu_Extru(l_Extru03+l_Extru04);
    translate([x_corner+tol,l_Extru01,2*x_alu+l_Extru02])Alu_Extru(l_Extru03+l_Extru04);
    translate([0,l_Extru01/2,2*x_alu+l_Extru02])Alu_Extru(l_Extru03+l_Extru04);
    
    translate([x_corner-x_alu+tol,0,x_alu+l_Extru02])rotate([90,0,0])Alu_Te();
    translate([x_corner-x_alu+tol,l_Extru01+x_alu+1,x_alu+l_Extru02])rotate([90,0,0])Alu_Te();
    translate([-1,l_Extru01/2-x_alu,x_alu+l_Extru02])rotate([90,0,90])Alu_Te();
}


module Top(){
    translate([x_corner,-Wall,x_alu+l_Extru02+x_alu+l_Extru03+l_Extru04-Wall]){
        difference(){
            union(){
                cube([x_alu+Wall,l_Extru01+x_alu+2*Wall,2*Wall]);
                translate([-x_corner-tol,0,0])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,2*Wall]);
                translate([-x_corner-tol,0,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,2*Wall]);
                translate([-x_corner-tol,l_Extru01,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,2*Wall]);
                translate([-x_corner-tol,l_Extru01/2,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,2*Wall]);
            }
            translate([0,Wall,-tol])cube([x_alu+2*tol,x_alu+2*tol,Wall]);
            translate([0,Wall+l_Extru01,-tol])cube([x_alu+2*tol,x_alu+2*tol,Wall]);
            translate([-x_corner-tol,Wall+l_Extru01/2,-tol])cube([x_alu+2*tol,x_alu+2*tol,Wall]);
            
            translate([x_alu/2,x_alu/2+Wall,-tol])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([x_alu/2,x_alu/2+Wall+l_Extru01,-tol])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([x_alu/2-x_corner-tol,x_alu/2+Wall+l_Extru01/2,-tol])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        }
        
        difference(){
            union(){
                translate([-Wall,0,-2*Wall])cube([x_alu+2*Wall,x_alu+2*Wall,2*Wall]);
                translate([-Wall,l_Extru01,-2*Wall])cube([x_alu+2*Wall,x_alu+2*Wall,2*Wall]);
                translate([-x_corner-tol,l_Extru01/2,-2*Wall])cube([x_alu+Wall,x_alu+2*Wall,2*Wall]);
            }
            translate([0,Wall,-2*Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,2*Wall+tol]);
            translate([0,Wall+l_Extru01,-2*Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,2*Wall+tol]);
            translate([-x_corner-tol,Wall+l_Extru01/2,-2*Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,2*Wall+tol]);
        }
    }
}





module Basler(){
    x_Basler = 29.5;
    y_Basler = 29.5;
    z_Basler = 29.5;
    r_Basler = 28.5/2;
    h_Basler = 43;
    z1 = 2.5;
    z2 = 26.5;
    y = 4.5;

    color([1,0,0])translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,0])rotate([-180,0,180]){
    translate([-x_Basler/2,-y_Basler/2,0])cube([x_Basler,y_Basler,z_Basler]);
    translate([0,0,z_Basler])cylinder(r=r_Basler,h=h_Basler,$fn=Smoothness);
    
    translate([x_Basler/2,0,z1])rotate([0,90,0])cylinder(r=M3,h=4*Wall,$fn=Smoothness);
    translate([x_Basler/2,y_Basler/2-y,z2])rotate([0,90,0])cylinder(r=M3,h=4*Wall,$fn=Smoothness);
    translate([x_Basler/2,-y_Basler/2+y,z2])rotate([0,90,0])cylinder(r=M3,h=4*Wall,$fn=Smoothness);
    }

    
    
}
module IR_Cam_Holder(){
    r_CameraHolder = 54.5/2;
    x_pin = 2;
    y_pin = 3;
    translate([0,0,2*x_alu+l_Extru02+2/3*l_Extru03+l_Extru04]){
        
        difference(){
            union(){
                translate([x_corner+tol-Wall-tol,-Wall-tol,0])Holder_Slider();
                translate([x_corner+tol-Wall-tol,l_Extru01-Wall-tol,0])Holder_Slider();
                translate([-Wall-tol,l_Extru01/2-Wall-tol,0])Holder_Slider();   
            }
        
            translate([x_corner+x_alu/2,-Wall-M3,z_slider/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            
            translate([x_corner+x_alu/2,-Wall-M3,z_slider*3/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider*3/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider*3/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            
            translate([x_corner+x_alu/2-x_link/2-tol,x_alu,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_corner+x_alu/2-x_link/2-tol,l_Extru01-z_link-tol,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_alu-tol,(l_Extru01+x_alu)/2-x_link/2,-tol])cube([z_link,x_link+2*tol,z_slider+2*tol]);
        }

        translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,Wall])difference(){
            cylinder(r=r_CameraHolder+Wall,h=2*Wall,$fn=Smoothness);
            translate([0,0,Wall])cylinder(r=r_CameraHolder+tol,h=Wall+tol,$fn=Smoothness);
            translate([0,0,-tol])cylinder(r=r_CameraHolder-Wall+tol,h=2*Wall+tol,$fn=Smoothness);
            intersection(){
                translate([0,0,-tol])cylinder(r=r_CameraHolder+tol,h=2*Wall+tol,$fn=Smoothness);
                rotate([0,0,-90])translate([r_CameraHolder,r_CameraHolder,-tol])rotate([0,0,45])scale([1.5,1,1])cylinder(r=r_CameraHolder,h=2*Wall,$fn=4);
            }
        }

        translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,Wall])for ( i =[0:3]){
            rotate([0,0,i*90+22.5])translate([-x_pin/2,r_CameraHolder-y_pin,Wall])cube([x_pin,y_pin,Wall]);
        }
        
        difference(){
            union(){
                translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,Wall])rotate([0,0,90])translate([-(x_alu+2*Wall)/2-tol,0,0])cube([x_alu+2*Wall,65,2*Wall]);
                translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,Wall])rotate([0,0,21.6])translate([-(x_alu+2*Wall)/2-tol-3,0,0])cube([x_alu+2*Wall+6,90,2*Wall]);
                translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,Wall])mirror([0,1,0])rotate([0,0,21.6])translate([-(x_alu+2*Wall)/2-tol-3,0,0])cube([x_alu+2*Wall+6,90,2*Wall]);
            }
            
            translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,Wall-tol])cylinder(r=r_CameraHolder+Wall,h=2*Wall+2*tol,$fn=Smoothness);
            
            translate([x_corner+tol-Wall-tol-50,-Wall-tol-50,0])cube([x_alu+2*Wall+50,x_alu+2*Wall+50,100]);
            translate([x_corner+tol-Wall-tol-50,l_Extru01-Wall-tol,0])cube([x_alu+2*Wall+50,x_alu+2*Wall+50,100]);
        }
        
        
        difference(){
            union(){
                translate([-Wall-tol,-Wall-tol,0])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,Wall]);
                translate([0,-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                translate([0,l_Extru01-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                
                translate([-Wall-tol,-Wall-tol,z_slider-Wall])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,Wall]);
                translate([0,-Wall-tol,z_slider-Wall])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                translate([0,l_Extru01-Wall-tol,z_slider-Wall])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                
                if (Basler_Holder_Full==1){
                    translate([-Wall-tol,-Wall-tol,0])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,z_slider]);
                    translate([0,-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,z_slider]);
                    translate([0,l_Extru01-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,z_slider]);
                }
            }
            translate([x_corner+tol-Wall-tol,-Wall-tol,0])Holder_Slider_Neg();
            translate([x_corner+tol-Wall-tol,l_Extru01-Wall-tol,0])Holder_Slider_Neg();
            translate([-Wall-tol,l_Extru01/2-Wall-tol,0])Holder_Slider_Neg();
            
            translate([x_corner+x_alu/2-x_link/2-tol,x_alu,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_corner+x_alu/2-x_link/2-tol,l_Extru01-z_link-tol,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_alu-tol,(l_Extru01+x_alu)/2-x_link/2,-tol])cube([z_link,x_link+2*tol,z_slider+2*tol]);
            
            if (Basler_Holder_Full==1){
                translate([x_corner+x_alu/2,-Wall-M3,z_slider/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                
                translate([x_corner+x_alu/2,-Wall-M3,z_slider*3/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider*3/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider*3/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                
                //translate([-Wall-tol,-Wall-tol,z_slider-Wall])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,Wall]);
                //translate([0,-Wall-tol,-tol])cube([x_alu+tol+x_corner,x_alu+2*Wall,z_slider+2*tol]);
                //translate([0,l_Extru01-Wall-tol,z_slider-Wall])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
            }
        }
    }

}

module Basler_Holder(){
    translate([0,0,2*x_alu+l_Extru02+2/3*l_Extru03+l_Extru04]){
        
        difference(){
            union(){
                translate([x_corner+tol-Wall-tol,-Wall-tol,0])Holder_Slider();
                translate([x_corner+tol-Wall-tol,l_Extru01-Wall-tol,0])Holder_Slider();
                translate([-Wall-tol,l_Extru01/2-Wall-tol,0])Holder_Slider();   
            }
        
            translate([x_corner+x_alu/2,-Wall-M3,z_slider/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            
            translate([x_corner+x_alu/2,-Wall-M3,z_slider*3/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider*3/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider*3/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
            
            translate([x_corner+x_alu/2-x_link/2-tol,x_alu,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_corner+x_alu/2-x_link/2-tol,l_Extru01-z_link-tol,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_alu-tol,(l_Extru01+x_alu)/2-x_link/2,-tol])cube([z_link,x_link+2*tol,z_slider+2*tol]);
        }
    
            
        difference(){
            union(){
                translate([-Wall-tol,-Wall-tol,0])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,Wall]);
                translate([0,-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                translate([0,l_Extru01-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                
                translate([-Wall-tol,-Wall-tol,z_slider-Wall])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,Wall]);
                translate([0,-Wall-tol,z_slider-Wall])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                translate([0,l_Extru01-Wall-tol,z_slider-Wall])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
                
                if (Basler_Holder_Full==1){
                    translate([-Wall-tol,-Wall-tol,0])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,z_slider]);
                    translate([0,-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,z_slider]);
                    translate([0,l_Extru01-Wall-tol,0])cube([x_alu+tol+x_corner,x_alu+2*Wall,z_slider]);
                }
            }
            translate([x_corner+tol-Wall-tol,-Wall-tol,0])Holder_Slider_Neg();
            translate([x_corner+tol-Wall-tol,l_Extru01-Wall-tol,0])Holder_Slider_Neg();
            translate([-Wall-tol,l_Extru01/2-Wall-tol,0])Holder_Slider_Neg();
            
            translate([x_corner+x_alu/2-x_link/2-tol,x_alu,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_corner+x_alu/2-x_link/2-tol,l_Extru01-z_link-tol,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
            translate([x_alu-tol,(l_Extru01+x_alu)/2-x_link/2,-tol])cube([z_link,x_link+2*tol,z_slider+2*tol]);
            
            if (Basler_Holder_Full==1){
                translate([x_corner+x_alu/2,-Wall-M3,z_slider/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                
                translate([x_corner+x_alu/2,-Wall-M3,z_slider*3/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider*3/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider*3/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
                
                //translate([-Wall-tol,-Wall-tol,z_slider-Wall])cube([x_alu+2*Wall,l_Extru01+x_alu+2*Wall,Wall]);
                //translate([0,-Wall-tol,-tol])cube([x_alu+tol+x_corner,x_alu+2*Wall,z_slider+2*tol]);
                //translate([0,l_Extru01-Wall-tol,z_slider-Wall])cube([x_alu+tol+x_corner,x_alu+2*Wall,Wall]);
            }
        }
    
        difference(){
            union(){
                translate([x_corner+x_alu+Wall,-Wall-tol,0])cube([5,l_Extru01+x_alu+2*Wall,z_slider]);
                translate([x_corner+x_alu+Wall,(l_Extru01+x_alu)/2-z_slider/2,0])cube([5.7,z_slider,z_slider]);
            }
            translate([0,0,z_slider])Basler();
        }
        translate([x_alu+Wall-tol,(l_Extru01+x_alu)/3-Wall/2,0])cube([x_corner+tol,Wall,z_slider]);
        translate([x_alu+Wall-tol,(l_Extru01+x_alu)*2/3-Wall/2,0])cube([x_corner+tol,Wall,z_slider]);
    }
    
}

module Holder_Slider(){
    zz = z_slider;
    difference(){
        cube([x_alu+2*Wall,x_alu+2*Wall,zz]);
        translate([Wall-tol,Wall-tol,-tol])cube([x_alu+2*tol,x_alu+2*tol,zz+2*tol]);
    }
}


module Holder_Slider_Neg(){
    zz = z_slider;
    translate([Wall-tol,Wall-tol,-tol])cube([x_alu+2*tol,x_alu+2*tol,zz+2*tol]);
}




module Alu_Extru(length){
    color([0.1,0.1,0.1])difference(){
        cube([x_alu,x_alu,length]);
        translate([x_alu/2-alu_groove/2,-tol,-tol])cube([alu_groove,alu_groove,length+2*tol]);
        translate([x_alu,0,0])rotate([0,0,90])translate([x_alu/2-alu_groove/2,-tol,-tol])cube([alu_groove,alu_groove,length+2*tol]);
        translate([x_alu,x_alu,0])rotate([0,0,180])translate([x_alu/2-alu_groove/2,-tol,-tol])cube([alu_groove,alu_groove,length+2*tol]);
        translate([0,x_alu,0])rotate([0,0,270])translate([x_alu/2-alu_groove/2,-tol,-tol])cube([alu_groove,alu_groove,length+2*tol]);
    }
}
module Alu_Corner(){
    x = x_corner;
    y = x_alu;
    z = 1;
    color([0.8,0.8,0.8]){
        cube([x,y,z]);
        cube([y,x,z]);
    }
}
module Alu_Te(){
    x = x_corner;
    y = x_alu;
    z = 1;
    color([0.8,0.8,0.8]){
        cube([x,y,z]);
        translate([x/2-y/2,0,0])cube([y,x,z]);
    }
}



module LED_Holder(){
    x = l_Extru01-x_alu-2*Wall;
    y = x;
    z = Wall;
    zz = 10;
    hh = x_alu + 15;
    d = x_alu+Wall+R_LED;
    Dx = (x-2*d)/5;
    Dy = (x-2*d)/3.5;
    dd = [0,1,0,1,0,1,0,1];
    
    translate([x_alu+Wall,x_alu+Wall,hh]){
        difference(){
            union(){
                cube([x,y,z]);
                
                translate([-2*Wall,-2*Wall,-zz+Wall])cube([x_alu+2*Wall,x_alu+2*Wall,zz]);
                translate([x-x_alu,-2*Wall,-zz+Wall])cube([x_alu+2*Wall,x_alu+2*Wall,zz]);
                translate([-2*Wall,,y-x_alu,-zz+Wall])cube([x_alu+2*Wall,x_alu+2*Wall,zz]);
                translate([x-x_alu,y-x_alu,-zz+Wall])cube([x_alu+2*Wall,x_alu+2*Wall,zz]);
            }
            
            translate([-Wall-tol,-Wall-tol,-zz+Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,zz+2*tol]);
            translate([x-x_alu+Wall-tol,-Wall-tol,-zz+Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,zz+2*tol]);
            translate([-Wall-tol,y-x_alu+Wall-tol,-zz+Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,zz+2*tol]);
            translate([x-x_alu+Wall-tol,y-x_alu+Wall-tol,-zz+Wall-tol])cube([x_alu+2*tol,x_alu+2*tol,zz+2*tol]);
            
            translate([-Wall+x_alu/2,-tol,Wall-zz/2])rotate([90,0,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            translate([x+Wall-x_alu/2,-tol,Wall-zz/2])rotate([90,0,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            
            translate([-Wall+x_alu/2,x+tol,Wall-zz/2])rotate([-90,0,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            translate([x+Wall-x_alu/2,x+tol,Wall-zz/2])rotate([-90,0,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            
            translate([-tol,-Wall+x_alu/2,Wall-zz/2])rotate([0,-90,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            translate([-tol,x+Wall-x_alu/2,Wall-zz/2])rotate([0,-90,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            
            translate([x+tol,-Wall+x_alu/2,Wall-zz/2])rotate([0,90,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
            translate([x+tol,x+Wall-x_alu/2,Wall-zz/2])rotate([0,90,0])cylinder(r=M3,h=2*Wall,$fn=Smoothness);
           
            
            for ( i = [0:1:5]){
                for ( j = [0:1:3]){
                    color([1,0,0,])translate([d+  i*Dx, d + j*Dy + dd[i]*Dy/2, -tol])cylinder(r=r_LED,h=2*Wall,$fn=Smoothness);
                    color([1,0,0,])translate([d+  i*Dx, d + j*Dy + dd[i]*Dy/2, -tol])cylinder(r=R_LED,h=Wall-h_LED+tol,$fn=Smoothness);
                    
                    color([0,1,0,])translate([d+  i*Dx, d + j*Dy + dd[i+1]*Dy/2, -tol])cylinder(r=r_LED,h=2*Wall,$fn=Smoothness);
                    color([0,1,0,])translate([d+  i*Dx, d + j*Dy + dd[i+1]*Dy/2, -tol])cylinder(r=R_LED,h=Wall-h_LED+tol,$fn=Smoothness);
                }
            }
        }
    }
}

Opto_Height = 250;
w_Opto = 2*Wall;
r_Opto1 = l_Extru01/2+x_alu/2+10;
r_opto1 = r_Opto1-w_Opto;
alpha = 10;
x_LED_Holder = 15;
h_LED_Holder = 2*Wall;//sin(alpha)*x_LED_Holder;
h_LED_casing = 1.2;
r_Opto2 = r_Opto1-(cos(alpha)*x_LED_Holder);
r_opto2 = r_Opto2-w_Opto;
spacing_Opto = 5.5;
$fs=0.5;
facets = 360;

module Optogenetics(){
    difference(){
        union(){
            translate([x_corner+tol-Wall-tol,-Wall-tol,0])Holder_Slider();
            translate([x_corner+tol-Wall-tol,l_Extru01-Wall-tol,0])Holder_Slider();
            translate([-Wall-tol,l_Extru01/2-Wall-tol,0])Holder_Slider();   
        }
    
        translate([x_corner+x_alu/2,-Wall-M3,z_slider/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        
        translate([x_corner+x_alu/2,-Wall-M3,z_slider*3/4])rotate([-90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        translate([x_corner+x_alu/2,l_Extru01+x_alu+Wall,z_slider*3/4])rotate([90,0,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        translate([-Wall-M3,x_alu/2+l_Extru01/2,z_slider*3/4])rotate([0,90,0])cylinder(r=M3,h=3*Wall,$fn=Smoothness);
        
        translate([x_corner+x_alu/2-x_link/2-tol,x_alu,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
        translate([x_corner+x_alu/2-x_link/2-tol,l_Extru01-z_link-tol,-tol])cube([x_link+2*tol,z_link,z_slider+2*tol]);
        translate([x_alu-tol,(l_Extru01+x_alu)/2-x_link/2,-tol])cube([z_link,x_link+2*tol,z_slider+2*tol]);
    }
    
    translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,5.9])difference(){
        step = $fs;
        for ( i =[0:step:facets]){
            rotate([0,0,i])translate([r_Opto1,0,0])rotate([0,180+alpha,0])cube([x_LED_Holder,2*step,h_LED_Holder]);
        }
        
        

        for (i = [0:1:3])rotate([0,0,(i*90)+45-1.5*spacing_Opto]){
            for (j = [0:1:3]){
                rotate([0,0,j*spacing_Opto]){
//                    translate([r_Opto1-(cos(alpha)*x_LED_Holder)/2,0,h_LED_Holder/2+tol])rotate([0,180+alpha,0]){
//                        cylinder(r=r_LED,h=2*Wall,$fn=Smoothness);
//                        cylinder(r=R_LED,h=Wall-h_LED+tol,$fn=Smoothness);
                    translate([r_Opto1-(cos(alpha)*x_LED_Holder)/2,0,-4.8])rotate([0,alpha,0]){
                        cylinder(r=r_LED,h=3*Wall,$fn=Smoothness);
                        translate([0,0,h_LED_casing])cylinder(r=R_LED,h=Wall-h_LED+tol,$fn=Smoothness);
                    }
                }
            }
        }
        

        
        for (i = [45:15:180]){
                for (j = [1,-1]){
                    rotate([0,0,i*j])translate([r_Opto1-(cos(alpha)*x_LED_Holder)/2+4.5,0,-4.8])rotate([0,alpha,0])cylinder(r=1,h=3*Wall,$fn=30);
            }
        }
        
        
        translate([-(l_Extru01+x_alu)/2,-(l_Extru01+x_alu)/2,-z_slider/2+Wall]){
            translate([x_corner+tol-Wall-tol,-Wall-tol,0])cube([x_alu+2*Wall,x_alu+2*Wall,z_slider]);
            translate([x_corner+tol-Wall-tol,l_Extru01-Wall-tol,0])cube([x_alu+2*Wall,x_alu+2*Wall,z_slider]);
            translate([-Wall-tol,l_Extru01/2-Wall-tol,0])cube([x_alu+2*Wall,x_alu+2*Wall,z_slider]); 
        }
    }
      
    
    translate([(l_Extru01+x_alu)/2,(l_Extru01+x_alu)/2,z_slider/2-Wall]){
        for (i = [0:1:3])rotate([0,0,(i*90)+45-1.5*spacing_Opto]){
            for (j = [0:1:3]){
                rotate([0,0,j*spacing_Opto]){
                    translate([r_Opto1-(cos(alpha)*x_LED_Holder)/2,0,h_LED_Holder/2])rotate([0,180+alpha,0]){
                        if (5mm_LED==1){
                            color(LED_Colour[j])LED();
                        }
                        if (Illumination == 1){
                            color(LED_Colour_Light[j])LED_Light();
                        }
                    }
                }
            }
        }    
    }
}




module LED(){
R_LED = 5.9/2;
H_LED = 1;
r_LED = 5/2;
h_LED = 7.7;
HH = Opto_Height;
aa = 15/2;
    cylinder(r=R_LED,h=H_LED,$fn=60);
    translate([0,0,H_LED])cylinder(r=r_LED,h=h_LED,$fn=60);
    translate([0,0,H_LED+h_LED])sphere(r=r_LED, $fn=60);
}
    
module LED_Light(){
R_LED = 5.9/2;
H_LED = 1;
r_LED = 5/2;
h_LED = 7.7;
HH = Opto_Height;
aa = 15;
    translate([0,0,H_LED+h_LED])cylinder(r1=r_LED, r2=r_LED+sin(aa)*HH, h=HH, $fn=60);
}
