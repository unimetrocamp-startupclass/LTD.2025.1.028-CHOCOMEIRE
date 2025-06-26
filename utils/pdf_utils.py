from fpdf import FPDF
import os

class PedidoPDF(FPDF):
    def header(self):
        if os.path.exists("static/Logo.Chocomeire.jpg"):
            self.image("static/Logo.Chocomeire.jpg", x=10, y=8, w=35)
            self.ln(30)

        self.set_font("Arial", "B", 16)
        self.set_text_color(91, 64, 51)
        self.cell(0, 10, "Pedido ChocoMeire", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(130, 130, 130)
        self.cell(0, 10, "Obrigada por sua compra!", 0, 0, "C")

def gerar_pdf_pedido(pedido):
    pdf = PedidoPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    cliente = pedido.cliente

    # Dados do pedido
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Pedido #{pedido.id}", ln=True)
    pdf.cell(0, 10, f"Cliente: {cliente.nome}", ln=True)
    pdf.cell(0, 10, f"Email: {cliente.email}", ln=True)
    pdf.cell(0, 10, f"Status: {pedido.status}", ln=True)
    pdf.cell(0, 10, f"Data: {pedido.data_criacao.strftime('%d/%m/%Y %H:%M')}", ln=True)
    pdf.ln(5)

    # Cabeçalho
    pdf.set_fill_color(248, 183, 206)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B", 11)

    col_widths = [60, 30, 60, 30]
    headers = ["Produto", "Qtd", "Sabores", "Subtotal"]
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
    pdf.ln()

    # Conteúdo da tabela
    pdf.set_font("Arial", "", 11)
    total = 0

    for item in pedido.itens:
        produto = item.produto
        subtotal = produto.preco * item.quantidade
        total += subtotal

        # Preparar os textos
        nome = produto.nome
        qtd = str(item.quantidade)
        sabores = item.sabores or "Nenhum"
        valor = f"R${subtotal:.2f}"

        # Calcular altura necessária
        line_height = 6
        max_lines = max(
            len(pdf.multi_cell(col_widths[0], line_height, nome, border=0, align='L', split_only=True)),
            len(pdf.multi_cell(col_widths[2], line_height, sabores, border=0, align='L', split_only=True))
        )
        row_height = line_height * max_lines

        y_start = pdf.get_y()
        x_start = pdf.get_x()

        # Produto
        pdf.multi_cell(col_widths[0], line_height, nome, border=1)
        x1 = x_start + col_widths[0]
        pdf.set_xy(x1, y_start)

        # Qtd
        pdf.multi_cell(col_widths[1], row_height, qtd, border=1, align='C')
        x2 = x1 + col_widths[1]
        pdf.set_xy(x2, y_start)

        # Sabores
        pdf.multi_cell(col_widths[2], line_height, sabores, border=1)
        x3 = x2 + col_widths[2]
        pdf.set_xy(x3, y_start)

        # Subtotal
        pdf.multi_cell(col_widths[3], row_height, valor, border=1, align='R')

    # Total
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(91, 64, 51)
    pdf.cell(0, 10, f"Total do Pedido: R${total:.2f}", ln=True)

    filename = f"static/pedido_{pedido.id}.pdf"
    pdf.output(filename)
    return filename