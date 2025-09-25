module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './theme/templates/**/*.html',
    './users/templates/**/*.html',
    './core/templates/**/*.html',
    './content/templates/**/*.html',
    './**/forms.py',
    './static/src/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#38a169',
          DEFAULT: '#2f855a',
          dark: '#276749',
        },
        secondary: {
          light: '#f6ad55',
          DEFAULT: '#ed8936',
          dark: '#dd6b20',
        },
        islamic: {
          gold: '#d4af37',
          green: '#228B22',
          navy: '#000080',
        },
      },
      fontFamily: {
        arabic: ['"Amiri"', '"Traditional Arabic"', 'serif'],
        sans: [
          'Inter',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          '"Noto Sans"',
          'sans-serif',
        ],
        serif: [
          '"Amiri"',
          'Georgia',
          'Cambria',
          '"Times New Roman"',
          'Times',
          'serif',
        ],
      },
      boxShadow: {
        'islamic': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06), 0 0 0 3px rgba(34, 139, 34, 0.5)',
      },
      backgroundImage: {
        'mosque-pattern': "url('../static/images/mosque-pattern-light.png')",
        'mosque-pattern-dark': "url('../static/images/mosque-pattern-dark.png')",
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/line-clamp'),
  ]
}