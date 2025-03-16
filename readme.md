# Restack AI Python Examples
==Kaiser–Bessel-derived (KBD) window==
[[File:Kbd-window.svg|right|401px]]
A related window function is the '''Kaiser–Bessel-derived (KBD)''' window, which is designed to be suitable for use with the [[modified discrete cosine transform]] (MDCT). The KBD window function is defined in terms of the Kaiser window of length ''N''+1, by the formula''':'''
:<math>
d_n =

\begin{cases}

\sqrt{\frac{\sum_{i=0}^{n} w[i]} {\sum_{i=0}^N w[i]}}
 & \mbox{if } 0 \leq n < N \\

\sqrt{\frac{\sum_{i=0}^{2N-1-n} w[i]} {\sum_{i=0}^N w[i]}}
 & \mbox{if } N \leq n \leq 2N-1 \\

0 & \mbox{otherwise}. \\

\end{cases}
</math>

This defines a window of length 2''N'', where by construction ''d''<sub>''n''</sub> satisfies the Princen-Bradley condition for the MDCT (using the fact that {{math|''w''{{sub|''N''−''n''}} {{=}} ''w''{{sub|''n''}}}}): {{math|''d''{{sub|''n''}}<sup>2</sup> + (''d''{{sub|''n''+''N''}})<sup>2</sup> {{=}} 1}} (interpreting ''n'' and ''n''&nbsp;+&nbsp;''N'' [[modular arithmetic|modulo]] 2''N''). The KBD window is also symmetric in the proper manner for the MDCT: ''d''<sub>''n''</sub>&nbsp;=&nbsp;''d''<sub>2''N''−1−''n''</sub>.

===Applications===
The KBD window is used in the [[Advanced Audio Coding]] digital audio format.
This repository contains various examples demonstrating how to use the Restack AI Python SDK. These examples are designed to help you get started with Restack AI and showcase different features and use cases.

This repository is organized into two sections:

- [Official examples](/): Actively maintained and tested by the Restack team
- [Community](/community) examples: Contributed by the community and may not be regularly updated

## Prerequisites

- Python 3.12 or higher
- Uv (for dependency management)

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/restackio/examples-python
   cd examples-python
   ```

2. Navigate to the example you want to explore:

   ```bash
   cd examples-python/<example-name>
   ```

3. Follow the specific instructions in each example's README file.

## Running Restack in Docker

To run Restack locally using Docker, you have two options:

Using `docker run`:

```bash
docker run -d --pull always --name restack -p 5233:5233 -p 6233:6233 -p 7233:7233 -p 9233:9233 ghcr.io/restackio/restack:main
```

This will force repulling and rebuilding.

After running either of these commands, the Restack UI will be available at http://localhost:5233

## Contributing

We welcome contributions to this repository. If you have an example you'd like to add or improvements to existing examples, please feel free to submit a pull request.
