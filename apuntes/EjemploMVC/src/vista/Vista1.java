package vista;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

import controlador.Controlador;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Vista1 extends JFrame {

	private JPanel contentPane;
	private Controlador controlador;
	private JTextField textField;
	private JButton btnBoton;

	public Vista1(Controlador controlador ) {
		this.setControlador(controlador);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 276, 201);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMiPrimeraVentana = new JLabel("Mi primera ventana");
		lblMiPrimeraVentana.setBounds(84, 11, 137, 24);
		contentPane.add(lblMiPrimeraVentana);
		
		JLabel lblUnLabel = new JLabel("Un label: ");
		lblUnLabel.setBounds(52, 57, 73, 14);
		contentPane.add(lblUnLabel);
		
		textField = new JTextField();
		textField.setBounds(135, 54, 86, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		btnBoton = new JButton("BOTON");
		btnBoton.addActionListener(this.getControlador());
		btnBoton.setBounds(84, 98, 89, 23);
		contentPane.add(btnBoton);
	}

	public Controlador getControlador() {
		return controlador;
	}

	public void setControlador(Controlador controlador) {
		this.controlador = controlador;
	}

	public JTextField getTextField() {
		return textField;
	}

	public void setTextField(JTextField textField) {
		this.textField = textField;
	}

	public JButton getBtnBoton() {
		return btnBoton;
	}

	public void setBtnBoton(JButton btnBoton) {
		this.btnBoton = btnBoton;
	}
}
