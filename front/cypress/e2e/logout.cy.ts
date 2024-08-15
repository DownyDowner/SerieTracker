describe('Déconnexion', () => {

  beforeEach(() => {
    cy.visit('/');
    cy.get('[data-cy="username-input"]').type('boris');
    cy.get('[data-cy="password-input"]').type('test');
    
    cy.get('[data-cy="login-button"]').click({ force: true });
    
    cy.url().should('include', '/home');
  });

  it('Déconnexion réussie', () => {
    cy.get('[data-cy="logout-button"]').click();
    cy.url().should('include', '/');
  });

});
