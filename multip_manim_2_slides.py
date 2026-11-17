from manim import *
from manim_slides import Slide

class MultiplicacaoRelativosSlides(Slide):
    def pausar_com_play(self):
        # Criação de um pequeno ícone de reprodução (triângulo estilizado)
        triangulo = Triangle(fill_opacity=0.6, fill_color=PURE_GREEN, stroke_width=0)
        triangulo.scale(0.2)
        triangulo.rotate(-90 * DEGREES)  # Aponta o triângulo para a direita
        
        circulo = Circle(
            radius=triangulo.width, 
            color=PURE_GREEN,
            stroke_opacity=0.6,
            fill_color=PURE_GREEN,     # Cor do preenchimento interno
            fill_opacity=0.2,
            stroke_width=5
        ).move_to(triangulo.get_center()).shift(LEFT * 0.05)
        
        icone_play = VGroup(circulo, triangulo)
        # Posicionamento no canto inferior direito do ecrã
        icone_play.to_corner(DR, buff=0.6).shift(UP * 0.8)

        # 1. Surge discretamente no ecrã
        self.play(FadeIn(icone_play, scale=0.8), run_time=0.4)
        
        # 2. Ponto de paragem da apresentação
        self.next_slide()
        
        # 3. Assim que o utilizador avança, o ícone desaparece
        self.play(FadeOut(icone_play, scale=0.8), run_time=0.3)

    def construct(self):
        # Configuração de cores e logo
        mycolor = ManimColor('#071E25')
        self.camera.background_color = mycolor
        
        img = ImageMobject('ifes.jpeg')
        img.scale(1)  
        img.shift(3.3 * DOWN + 5.6 * RIGHT)  
        self.add(img) 

        # --- SLIDE 1: Abertura e Identificação ---
        titulo = Tex("Multiplicação de Números Naturais", font_size=48).to_edge(UP, buff=0.3)
        turma = Tex("Educimat", font_size=35).next_to(titulo, DOWN, buff=0.15)
        prof = Tex("Prof. Alex Jordane", font_size=30).next_to(turma, DOWN, buff=0.15)
        
        self.play(Write(titulo))
        self.play(Write(turma))
        self.play(Write(prof))

        # --- Bloco de Instruções de Navegação ---
        guia_navegacao = VGroup(
            Tex(r"\textbf{Instruções de navegação:}", font_size=28, color=GREEN_C),
            Tex(r"$\bullet$ Pressione a \textbf{Seta para a Direita} para avançar.", font_size=24),
            Tex(r"$\bullet$ Pressione a \textbf{Seta para a Esquerda} para voltar um slide.", font_size=24),
            Tex(r"$\bullet$ Pressione \textbf{Barra de Espaço} para iniciar o slide atual do começo.", font_size=24),
            Tex(r"$\bullet$ Pressione \textbf{F} para entrar em tela cheia.", font_size=24),
            Tex(r"$\bullet$ Pressione \textbf{ESC} para sair da tela cheia.", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(DOWN, buff=1.2)

        self.play(FadeIn(guia_navegacao, shift=UP * 0.3))
        
        self.pausar_com_play()

        # --- SLIDE 2: Multiplicação de Números Naturais ---
        self.play(FadeOut(guia_navegacao))

        operacao_principal = MathTex(r"2 \cdot 3", font_size=52).next_to(prof, DOWN, buff=0.4)
        
        reta = NumberLine(
            x_range=[-7, 7, 1],
            length=11,
            color=BLUE_D,
            include_numbers=True,
            numbers_to_include=range(-6, 7)
        ).shift(DOWN * 2)

        ponto_3 = Dot(reta.n2p(3), color=YELLOW, radius=0.08)

        self.play(Write(operacao_principal))
        self.play(Create(reta))
        self.play(FadeIn(ponto_3, scale=0.5))

        p_inicio = reta.n2p(0)
        p_fim = reta.n2p(3)
        vetor1 = Arrow(
            start=p_inicio,
            end=p_fim,
            buff=0,
            color=GREEN,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(FadeIn(vetor1))
        self.play(vetor1.animate.shift(UP * 1.2), run_time=1)
        self.play(
            vetor1.animate.rotate(
                angle=25 * DEGREES, 
                about_point=vetor1.get_start()
            ).shift(DOWN * 1.2),
            run_time=1.2
        )
        self.play(
            vetor1.animate.rotate(
                angle=-25 * DEGREES, 
                about_point=reta.n2p(0)
            ),
            run_time=1
        )

        texto_passo1 = MathTex(r"1 \cdot 3 = 3", color=GREEN, font_size=40)
        texto_passo1.next_to(vetor1, UP, buff=0.4)
        self.play(Write(texto_passo1))
        
        vetor2 = vetor1.copy()
        
        self.play(vetor2.animate.set_color(ORANGE).shift(UP * 1.2), run_time=1)
        
        deslocamento = reta.n2p(3) - reta.n2p(0)

        self.play(vetor2.animate.shift(deslocamento), run_time=1.2)

        self.play(
            vetor2.animate.rotate(
                angle=25 * DEGREES, 
                about_point=vetor2.get_start()
            ).shift(DOWN * 1.2),
            run_time=1.2
        )
        self.play(
            vetor2.animate.rotate(
                angle=-25 * DEGREES, 
                about_point=vetor2.get_start()
            ),
            run_time=1
        )

        ponto_6 = Dot(reta.n2p(6), color=YELLOW, radius=0.08)
        texto_passo2 = MathTex(r"2 \cdot 3 = 6", color=ORANGE, font_size=40)
        texto_passo2.next_to(vetor2, UP, buff=0.4)

        self.play(FadeIn(ponto_6, scale=0.5))
        self.play(Write(texto_passo2))
        
        self.pausar_com_play()

        # --- SLIDE 3: Transição para os Negativos: (-2) · 3 = -6 ---
        bloco_vetores = VGroup(vetor1, vetor2)

        self.play(
            FadeOut(texto_passo1),
            FadeOut(texto_passo2),
            FadeOut(ponto_3),
            FadeOut(ponto_6)
        )

        titulo2 = Tex("Multiplicação de Números Negativos", font_size=48).to_edge(UP, buff=0.3)
        self.play(Transform(titulo, titulo2))

        ponto_menos6 = Dot(reta.n2p(-6), color=YELLOW, radius=0.08)
        texto_menos2_vezes_3 = MathTex(r"(-2) \cdot 3 = -6", color=ORANGE, font_size=42)
        
        operacao_negativa1 = MathTex(r"(-2) \cdot 3", font_size=52).move_to(operacao_principal)

        self.play(Transform(operacao_principal, operacao_negativa1))

        text_multiplicacao_negativa = Tex(r"A multiplicação de um número negativo $(-2)$ por um número positivo $(3)$ pode ser interpretada como a rotação, em torno da origem, do resultado da multiplicação de $2 \cdot 3$. Esse processo leva a um número negativo.",
            font_size=28,
            color=GREEN_C
        ).next_to(operacao_principal, DOWN, buff=0.5)  

        self.play(FadeIn(text_multiplicacao_negativa, scale=0.8))

        self.pausar_com_play()

        # --- SLIDE 4: Primeiro Giro: (-2) · 3 = -6 ---
        self.play(FadeOut(text_multiplicacao_negativa))

        self.play(
            Rotate(
                bloco_vetores,
                angle=PI,
                about_point=reta.n2p(0)
            ),
            run_time=2.2,
        )
        texto_menos2_vezes_3.next_to(bloco_vetores, UP, buff=0.5)
        self.play(
            FadeIn(ponto_menos6, scale=0.5),
            Write(texto_menos2_vezes_3)
        )

        self.pausar_com_play()

        # --- SLIDE 5: Segundo Giro: (-2) · (-3) = 6 ---
        self.play(
            FadeOut(texto_menos2_vezes_3),
            FadeOut(ponto_menos6)
        )

        operacao_negativa2 = MathTex(r"(-2) \cdot (-3)", font_size=52).move_to(operacao_principal)

        self.play(Transform(operacao_principal, operacao_negativa2))

        text_multiplicacao_negativa2 = Tex(
            r"A multiplicação de um número negativo $(-2)$ por um número negativo $(-3)$ pode ser interpretada como a rotação, em torno da origem, do resultado da multiplicação de $(-2) \cdot 3$. Esse processo leva a um número positivo.",
            font_size=28,
            color=GREEN_C
            ).next_to(operacao_negativa2, DOWN, buff=0.5)
        
        self.play(FadeIn(text_multiplicacao_negativa2, scale=0.8))
        
        self.pausar_com_play()

        # --- SLIDE 6: Resultado Final: (-2) · (-3) = 6 ---        
        self.play(FadeOut(text_multiplicacao_negativa2))
        
        self.play(
            Rotate(
                bloco_vetores,
                angle=-PI,
                about_point=reta.n2p(0)
            ),
            run_time=2.2
        )

        ponto_final6 = Dot(reta.n2p(6), color=YELLOW, radius=0.08)
        texto_final = MathTex(r"(-2) \cdot (-3) = 6", color=YELLOW, font_size=42)
        texto_final.next_to(bloco_vetores, UP, buff=0.5)

        self.play(
                    FadeIn(ponto_final6, scale=0.5),
                    Write(texto_final)
                )
        # Pausa para apreciação do resultado final antes do encerramento
        self.pausar_com_play()

        # --- SLIDE FINAL: Encerramento ---
        # Despedida suave dos elementos da tela
        self.play(
            FadeOut(reta),
            FadeOut(bloco_vetores),
            FadeOut(ponto_final6),
            FadeOut(texto_final),
            FadeOut(operacao_principal)
        )

        mensagem_fim = VGroup(
            Tex(r"\textbf{Fim da apresentação}", font_size=44, color=GREEN_C),
            Tex(r"Pressione a \textbf{Seta para a Direita} para reiniciar a apresentação.", font_size=28)
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(mensagem_fim, shift=UP * 0.2))
        
        # Último ponto de parada dos slides
        triangulo = Triangle(fill_opacity=0.6, fill_color=PURE_GREEN, stroke_width=0)
        triangulo.scale(0.2)
        triangulo.rotate(-90 * DEGREES)  # Aponta o triângulo para a direita
                
        circulo = Circle(
            radius=triangulo.width, 
            color=PURE_GREEN,
            stroke_opacity=0.6,
            fill_color=PURE_GREEN,     # Cor do preenchimento interno
            fill_opacity=0.2,
            stroke_width=5
            ).move_to(triangulo.get_center()).shift(LEFT * 0.05)
                
        icone_play = VGroup(circulo, triangulo)
            # Posicionamento no canto inferior direito do ecrã
        icone_play.to_corner(DR, buff=0.6).shift(UP * 0.8)

        # 1. Surge discretamente no ecrã
        self.play(FadeIn(icone_play, scale=0.8), run_time=0.4)