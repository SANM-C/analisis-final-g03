"""Esqueleto generado por spec2code. Módulo: Arena de combate

NO es una solución: son clases y firmas con TODO. Completa la lógica, audita cada
clase contra la spec y corrige la SPEC (no este archivo) cuando el error venga de ella.
"""
from __future__ import annotations



class Personaje:
    """Personaje. Trazabilidad: RN-01, RN-02, RN-03, RN-04, RN-05, RN-06, RN-07, RN-08, RN-09, RN-10, RN-11."""

    def __init__(self, puntos_vida: int, atributo_ataque: int) -> None:
        self.puntos_vida: int = puntos_vida  # TODO: encapsulamiento (propiedades)
        self.atributo_ataque: int = atributo_ataque  # TODO: encapsulamiento (propiedades)
        self.personaje: Personaje | None = None  # asociacion: enfrentamiento_con ()

    def iniciar_combate(self) -> None:
        """Inicia el combate con otro personaje. (RF-02, RF-03, RF-04, RF-05)."""
        raise NotImplementedError("TODO: implementar Personaje.iniciar_combate")

    def realizar_accion(self) -> None:
        """Realiza una acción durante el turno. (RF-06, RF-07, RF-08, RF-09, RF-10, RF-11, RF-12, RF-13, RF-14, RF-15, RF-16)."""
        raise NotImplementedError("TODO: implementar Personaje.realizar_accion")
