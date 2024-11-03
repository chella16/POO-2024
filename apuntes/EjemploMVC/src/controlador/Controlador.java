package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;

import modelo.Modelo;
import vista.Vista1;

public class Controlador implements ActionListener {

	private Vista1 vista;
	private Modelo modelo;
	
	public Controlador() {
		super();
		this.setModelo(new Modelo());
		this.setVista(new Vista1(this));

	}
	
	@Override
	public void actionPerformed(ActionEvent arg0) {
		JButton btn = (JButton) arg0.getSource();
		if (btn.getText().equals("BOTON")) {
			String texto = this.getVista().getTextField().getText();
			System.out.println(texto);
			
			new Controlador2();
		}
		
	}

	public Vista1 getVista() {
		return vista;
	}

	public void setVista(Vista1 vista) {
		this.vista = vista;
	}

	public Modelo getModelo() {
		return modelo;
	}

	public void setModelo(Modelo modelo) {
		this.modelo = modelo;
	}



}
