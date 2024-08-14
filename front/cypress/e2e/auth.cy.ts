describe('Tests de la page de connexion', () => {

  beforeEach(() => {
    cy.visit('/');
  });

  it('Connexion réussie avec des identifiants valides', () => {
    cy.get('[data-cy="username-input"]').type('boris');
    cy.get('[data-cy="password-input"]').type('test');
    
    cy.get('[data-cy="login-button"]').click({ force: true });
    
    cy.url().should('include', '/home');
  });

  it('Échec de la connexion avec des identifiants invalides', () => {
    cy.get('[data-cy="username-input"]').type('invalidUsername');
    cy.get('[data-cy="password-input"]').type('invalidPassword');
    
    cy.get('[data-cy="login-button"]').click({ force: true });
    
    cy.get('[data-cy="error-message"]').should('contain', 'Échec de la connexion. Veuillez vérifier vos identifiants et réessayer');
  });

  it('Accès à la page de création de compte', () => {
    cy.get('[data-cy="create-account-button"]').click();
    cy.url().should('include', '/signup');
  });

});
