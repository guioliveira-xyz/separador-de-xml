import org
import stats
import VAR

def main():
    print('Iniciando a organização dos XMLS...')
    print('')
    org.separar_xml()

    print('\nProcessando estatísticas de venda...')
    print('')
    info = stats.processar_xmls()
    print('=' * 30)
    stats.exibir_info('TOTAL', info)
    print('=' * 30)
    stats.exibir_info('varejo', info)
    print('=' * 30)
    stats.exibir_info('atacado', info)
    print('=' * 30)

    print('\nProcessando vendas de produtos estratégicos...')
    print('')
    VAR.processar_var()

if __name__ == "__main__":
    main()