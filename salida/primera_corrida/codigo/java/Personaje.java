// Esqueleto generado por spec2code. Módulo: Arena de combate
// NO es una solución: clases y firmas con TODO. Completa la lógica y audita contra la spec.
package rpgmanager.arenadecombate;

/** Personaje. Trazabilidad: RN-01, RN-02, RN-03, RN-04, RN-05, RN-06, RN-07, RN-08, RN-09, RN-10, RN-11. */
public class Personaje {
    private int puntosVida;
    private int atributoAtaque;
    private Personaje personaje; // asociacion: enfrentamiento_con ()

    public Personaje(int puntosVida, int atributoAtaque) {
        this.puntosVida = puntosVida;
        this.atributoAtaque = atributoAtaque;
    }

    // TODO: getters y setters (encapsulamiento)

    /** Inicia el combate con otro personaje. (RF-02, RF-03, RF-04, RF-05). */
    public void iniciarCombate() {
        throw new UnsupportedOperationException("TODO: implementar Personaje.iniciar_combate");
    }

    /** Realiza una acción durante el turno. (RF-06, RF-07, RF-08, RF-09, RF-10, RF-11, RF-12, RF-13, RF-14, RF-15, RF-16). */
    public void realizarAccion() {
        throw new UnsupportedOperationException("TODO: implementar Personaje.realizar_accion");
    }
}
