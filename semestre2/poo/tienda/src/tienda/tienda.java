package tienda;
import java.util.*;

public class tienda {

	public static void main(String[] args) {

		System.out.println("[+] Bienvenido a la tienda.");
		
		producto pc = new producto();
        
        System.out.println("Nuestros Productos son: ");
        System.out.println(pc.nombreProducto[0]);
        System.out.println(pc.nombreProducto[1]);
        System.out.println(pc.nombreProducto[2]);
        System.out.println(pc.nombreProducto[3]);
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("Que Producto Requiere? ");
        String pedidoCliente = input.next();      
        
        System.out.println("Cuantos " + pedidoCliente +" Quiere? ");
        int  cantidadPedido = input.nextInt();
       
        //pc.nombreProducto = pedidoCliente;
        
        pc.cantidadVendida = cantidadPedido;
        pc.stockProducto = (pc.stockMax - cantidadPedido);
        
        
        
        double precioVenta = (pc.precioProducto * cantidadPedido);
        
        System.out.println("\n-------------------------------------------------------");
        System.out.println("[+] El total de la compra es: " + precioVenta);
        System.out.println("-------------------------------------------------------\n");
        
        if (pc.stockProducto <= 5) {
        	System.out.println("Quedan " + pc.stockProducto + " " + pedidoCliente);
        	int surtirProducto = (pc.stockMax - pc.stockProducto );
        	System.out.println("Se debe surtir este producto pidiendo: " + surtirProducto);
        	
        	pc.stockProducto = (pc.stockProducto + surtirProducto);
        	
        } else {
        	System.out.println("Quedan " + pc.stockProducto + " " + pedidoCliente);
        	System.out.println("Estamos bien de Inventario para este producto.");
        }
        

	}
}
