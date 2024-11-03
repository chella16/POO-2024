package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import vista.Vista2;

public class Controlador2 implements ActionListener {

	private Vista2 vista;

	public Controlador2() {
		super();
		this.setVista(new Vista2(this));
		this.getVista().setVisible(true);

	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
	}

	public Vista2 getVista() {
		return vista;
	}

	public void setVista(Vista2 vista2) {
		this.vista = vista2;
	}

}
