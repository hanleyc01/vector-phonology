---
title: "Notes on Introduction to Semantic Pointer Architecture"
output: html_document
date: "2022-11-15"
---

Notes are taken from [here](https://www.nengo.ai/nengo-spa/v1.3.0/user-guide/spa-intro.html)

# Introduction

-   The Semantic Pointer hypothesis: "Higher-level cognitive functions in biological systems are made possible by Semantic Pointers. Semantic Pointers are neural representations that carry partial semantic content and are composable into the representational structures necessary to support complex cognition."
    -   In other words, SPs are a hypothesized entity that functions within cognition to abstract away from lower-level sensory input (etc.) and deal with these things more abstractly, and less cost-heavy.
-   SPA is from [How to build a brain](https://www.amazon.com/How-Build-Brain-Architecture-Architectures/dp/0199794545) which describes the architecture under four main topics:
    1.  Semantics, which discusses how SPs are generated from information that inpinges on the senses
    2.  Syntax, which demonstrates how very large structures can be encoded by binding SPs to one another
    3.  Control, how the role of the basal ganglia and other structures in routing information throughout the brain to control cognitive tasks
    4.  Learning and memory, which describes how the SPA includes "adaptability ... showing how detailed spiking timingg during learning can be incorporated into the basal ganglia model using a biologically plausible STDP-like rule."

# Structured representations

-   SPA uses a Vector Symbolic Architecture to capture concepts, which can be combined with linear and non-linear operations "to bind the concept vectord and build structured representations"
-   The specific opoerations by SPA usually use random vectors of unit-length, and three basic operations
    1.  *Superposition*: Two vectors $\vec{v}$ and $\vec{w}$ can be combined in a union-like operation by simple addition as $\vec{u} = \vec{v} + \vec{w}$. The resulting vector will be similar to both of the original vectors.

    2.  *Binding*: The binding has to produce a vector that is dissimilar to both the original vectors and allows to recover on eof the original vectors given the other one. Circular convolution for this purpose is defined as:
    $$
    \vec{u} = \vec{v} \circledast \vec{w} \space : u_i = \sum^{D}_{j=1} v_j w_{(i-j)\space mod \space D}
    $$
        where $D$ is the dimensionality of the vectors.

    3.  *Unbinding*: To unbind a vector from a circular convolution, another circular convolution with the approximate inverse of one of the vectors can be used: $\vec{v} \approx \vec{u} \circledast \vec{w}^+$. The approximate inverse is given by reordering the vector components:

        $\vec{w}^+ = (w_1, w_D, w_{D-1}, …, w_2)^T$.

        -   Circular convolution is associative, commutative, and distributive.

## Example

Given the vectors *red, blue, square* and *circle*; we can represent *red square* with *blue circle* as:

$$
\vec{v} = \mathrm{Red} \circledast \mathrm{Square} + \mathrm{Blue} \circledast \mathrm{Circle}
$$

If we want to know the color of the square,

$$
\vec{v} \circledast \mathrm{Square} = \mathrm{Red} \circledast \mathrm{Square} \circledast \mathrm{Square}^+ + \mathrm{Blue} \circledast \mathrm{Circle} \circledast \mathrm{Square}^+ \approx \mathrm{Red} + noise
$$
