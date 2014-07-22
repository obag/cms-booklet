\documentclass[((( __language )))]{cms-contest}

\usepackage[((( fontenc )))]{fontenc}
\usepackage[((( inputenc )))]{inputenc}
\usepackage[((( __language )))]{babel}

\begin{document}
	\begin{contest}{(((name)))}{(((location)))}{(((date)))}
		\setContestLogo{(((logo)))}
		((* for __problem in __problems *))
			((( __problem )))
		((* endfor *))
	\end{contest}
\end{document}