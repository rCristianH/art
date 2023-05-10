 void Form1_Load(object sender, EventArgs e)
{
    // Registra el evento KeyDown para el formulario.
    this.KeyDown += new KeyEventHandler(Form1_KeyDown);
}
 void Form1_KeyDown(object sender, KeyEventArgs e)
{
    // Agrega la tecla presionada al ListBox.
    listBox1.Items.Add(e.KeyCode.ToString());
}
