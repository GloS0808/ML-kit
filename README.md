<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML-kit | Free Machine Learning Tools</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #4a6cf7;
            --primary-dark: #3a56d4;
            --secondary: #6c757d;
            --dark: #1d2144;
            --light: #f8f9fa;
            --success: #28a745;
            --border-radius: 8px;
            --box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f7ff;
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header Styles */
        header {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            padding: 80px 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB2aWV3Qm94PSIwIDAgMTIwMCA4MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0iIzNBNTZENCIgZmlsbC1vcGFjaXR5PSIwLjEiPjxjaXJjbGUgY3g9IjQwMCIgY3k9IjQwMCIgcj0iMzAwIi8+PGNpcmNsZSBjeD0iODAwIiBjeT0iNDAwIiByPSIzMDAiLz48Y2lyY2xlIGN4PSI2MDAiIGN5PSIyMDAiIHI9IjMwMCIvPjxjaXJjbGUgY3g9IjYwMCIgY3k9IjYwMCIgcj0iMzAwIi8+PC9nPjwvc3ZnPg==');
            opacity: 0.3;
        }
        
        .logo {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 10px;
            display: inline-block;
        }
        
        .tagline {
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        
        .btn {
            display: inline-block;
            padding: 12px 30px;
            background-color: white;
            color: var(--primary);
            border-radius: var(--border-radius);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
            box-shadow: var(--box-shadow);
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }
        
        .btn-secondary {
            background-color: transparent;
            color: white;
            border: 2px solid white;
            margin-left: 10px;
        }
        
        .btn-secondary:hover {
            background-color: white;
            color: var(--primary);
        }
        
        /* Features Section */
        .section {
            padding: 80px 0;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .section-title h2 {
            font-size: 2.2rem;
            color: var(--dark);
            margin-bottom: 15px;
        }
        
        .section-title p {
            color: var(--secondary);
            max-width: 600px;
            margin: 0 auto;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .feature-card {
            background-color: white;
            border-radius: var(--border-radius);
            padding: 30px;
            box-shadow: var(--box-shadow);
            transition: var(--transition);
            text-align: center;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 20px;
        }
        
        .feature-card h3 {
            margin-bottom: 15px;
            color: var(--dark);
        }
        
        .feature-card p {
            color: var(--secondary);
        }
        
        /* About Section */
        .about {
            background-color: var(--light);
        }
        
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }
        
        .about-text h2 {
            font-size: 2rem;
            margin-bottom: 20px;
            color: var(--dark);
        }
        
        .about-text p {
            margin-bottom: 20px;
            color: var(--secondary);
        }
        
        .about-image {
            text-align: center;
        }
        
        .about-image img {
            max-width: 100%;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
        }
        
        /* Tools Section */
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
        }
        
        .tool-card {
            background-color: white;
            border-radius: var(--border-radius);
            padding: 25px;
            box-shadow: var(--box-shadow);
            transition: var(--transition);
            text-align: center;
        }
        
        .tool-card:hover {
            transform: translateY(-5px);
        }
        
        .tool-icon {
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 15px;
        }
        
        .tool-card h3 {
            margin-bottom: 10px;
            color: var(--dark);
        }
        
        .tool-card p {
            color: var(--secondary);
            font-size: 0.9rem;
        }
        
        /* CTA Section */
        .cta {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            text-align: center;
            padding: 80px 0;
        }
        
        .cta h2 {
            font-size: 2.2rem;
            margin-bottom: 20px;
        }
        
        .cta p {
            max-width: 600px;
            margin: 0 auto 30px;
            opacity: 0.9;
        }
        
        /* Footer */
        footer {
            background-color: var(--dark);
            color: white;
            padding: 50px 0 20px;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }
        
        .footer-column h3 {
            margin-bottom: 20px;
            font-size: 1.2rem;
        }
        
        .footer-column ul {
            list-style: none;
        }
        
        .footer-column ul li {
            margin-bottom: 10px;
        }
        
        .footer-column ul li a {
            color: #a0a7c2;
            text-decoration: none;
            transition: var(--transition);
        }
        
        .footer-column ul li a:hover {
            color: white;
        }
        
        .social-links {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
        
        .social-links a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            color: white;
            transition: var(--transition);
        }
        
        .social-links a:hover {
            background-color: var(--primary);
            transform: translateY(-3px);
        }
        
        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #a0a7c2;
            font-size: 0.9rem;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .about-content {
                grid-template-columns: 1fr;
            }
            
            .btn {
                display: block;
                margin: 10px auto;
                width: 80%;
                max-width: 250px;
            }
            
            .btn-secondary {
                margin-left: 0;
            }
            
            header {
                padding: 60px 0;
            }
            
            .section {
                padding: 60px 0;
            }
            /* AI Disclosure Styles */
            .ai-disclosure {
                background: rgba(255, 255, 255, 0.2);
                padding: 10px 20px;
                border-radius: 30px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 25px;
                font-size: 0.9rem;
                backdrop-filter: blur(5px);
            }
            
            .development-note {
                background: var(--light);
                padding: 20px;
                border-radius: var(--border-radius);
                border-left: 4px solid var(--ai-color);
                margin: 20px 0;
            }
            
            .development-note h3 {
                color: var(--ai-color);
                margin-bottom: 10px;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .ai-acknowledgement {
                background: rgba(138, 43, 226, 0.1);
                padding: 12px;
                border-radius: var(--border-radius);
                margin: 15px 0;
                font-size: 0.85rem;
                border: 1px solid rgba(138, 43, 226, 0.2);
            }
            
            .ai-acknowledgement i {
                color: var(--ai-color);
                margin-right: 5px;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1 class="logo">ML-kit</h1>
            <p class="tagline">Free and easy tools to create a machine learning system</p>
            <div class="ai-disclosure">
                <i class="fas fa-robot"></i>
                <span>AI-assisted development • All code tested and verified</span>
            </div>
            <a href="#" class="btn">Get Started</a>
            <a href="#" class="btn btn-secondary">View on GitHub</a>
        </div>
    </header>

    <!-- Features Section -->
    <section class="section">
        <div class="container">
            <div class="section-title">
                <h2>Why Choose ML-kit?</h2>
                <p>Our tools are designed to make machine learning accessible to everyone, regardless of experience level.</p>
            </div>
            <div class="features">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-lock-open"></i>
                    </div>
                    <h3>Completely Free</h3>
                    <p>All tools and resources are open source and free to use for any purpose.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-bolt"></i>
                    </div>
                    <h3>Easy to Use</h3>
                    <p>Simple APIs and clear documentation make implementation straightforward.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <h3>Community Driven</h3>
                    <p>Join a growing community of developers contributing to the project.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="section about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>About ML-kit</h2>
                    <p>ML-kit is an open-source project aimed at creating free and accessible machine learning tools. Our mission is to democratize AI by providing easy-to-use libraries and frameworks that lower the barrier to entry for developers of all skill levels.</p>
                    
                    <div class="development-note">
                        <h3><i class="fas fa-code"></i> Development Note</h3>
                        <p>This project utilized AI assistance during development. All generated code has been thoroughly tested and validated to ensure functionality and reliability.</p>
                    </div>
                    
                    <p>Whether you're a beginner looking to learn the basics or an experienced developer building production systems, ML-kit has tools to accelerate your machine learning projects.</p>
                    <a href="#" class="btn">Learn More</a>
                </div>
                <div class="about-image">
                    <!-- Placeholder for ML visualization -->
                    <div style="background: linear-gradient(135deg, #4a6cf7, #3a56d4); height: 300px; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem;">
                        ML Visualization Example
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Tools Section -->
    <section class="section">
        <div class="container">
            <div class="section-title">
                <h2>Available Tools</h2>
                <p>Explore our growing collection of machine learning tools and libraries.</p>
            </div>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3>Neural Networks</h3>
                    <p>Build and train neural networks with our intuitive API.</p>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>Data Preprocessing</h3>
                    <p>Clean, transform and prepare your data for ML models.</p>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">
                        <i class="fas fa-robot"></i>
                    </div>
                    <h3>Model Training</h3>
                    <p>Train models with just a few lines of code.</p>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <h3>Evaluation Tools</h3>
                    <p>Analyze model performance with comprehensive metrics.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta">
        <div class="container">
            <h2>Ready to Get Started?</h2>
            <p>Join the ML-kit community today and start building machine learning systems with our free tools.</p>
            <a href="#" class="btn">Download Now</a>
            <a href="#" class="btn btn-secondary">View Documentation</a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>ML-kit</h3>
                    <p>Free and easy tools to create a machine learning system.</p>
                    <div class="ai-acknowledgement">
                        <p><i class="fas fa-robot"></i> Built with AI assistance • Tested for reliability</p>
                    </div>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-github"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-discord"></i></a>
                        <a href="#"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>
                <!-- Other footer columns remain the same -->
            </div>
            <div class="copyright">
                <p>&copy; 2023 ML-kit. All rights reserved. | AI-assisted development with verified code quality</p>
            </div>
        </div>
    </footer>

    <script>
        // Simple animation for feature cards on scroll
        document.addEventListener('DOMContentLoaded', function() {
            const featureCards = document.querySelectorAll('.feature-card');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = 1;
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, { threshold: 0.1 });
            
            featureCards.forEach(card => {
                card.style.opacity = 0;
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                observer.observe(card);
            });
        });
    </script>
</body>
</html>
