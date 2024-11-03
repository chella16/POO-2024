package vista;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import controlador.Controlador2;

public class Vista2 extends JFrame {

	private JPanel contentPane;
	private Controlador2 controlador;


	public Vista2(Controlador2 controlador) {
		this.setControlador(controlador);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 275, 169);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblVista = new JLabel("VISTA 2");
		lblVista.setBounds(98, 46, 121, 14);
		contentPane.add(lblVista);
	}


	public Controlador2 getControlador() {
		return controlador;
	}


	public void setControlador(Controlador2 controlador) {
		this.controlador = controlador;
	}

}
